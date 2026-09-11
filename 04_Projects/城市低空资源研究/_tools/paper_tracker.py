#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动化论文追踪系统
支持 arXiv, Semantic Scholar 多源追踪
"""

import os
import sys
from pathlib import Path
from datetime import datetime, timedelta
from typing import List, Dict, Any
import yaml
import json
import time

# 设置标准输出编码为 UTF-8
if sys.platform == "win32":
    import codecs
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# 第三方库（需要安装）
try:
    import arxiv
    import requests
except ImportError:
    print("缺少依赖库，请运行: pip install arxiv requests pyyaml")
    sys.exit(1)


class PaperTracker:
    """论文追踪核心类"""

    def __init__(self, config_path: str = "paper_tracker_config.yaml"):
        """初始化追踪器"""
        self.config_path = Path(config_path)
        self.load_config()
        self.results = {
            "arxiv": [],
            "semantic_scholar": [],
            "metadata": {
                "timestamp": datetime.now().isoformat(),
                "total_papers": 0
            }
        }

    def load_config(self):
        """加载配置文件"""
        with open(self.config_path, 'r', encoding='utf-8') as f:
            self.config = yaml.safe_load(f)
        print(f"✅ 配置加载成功: {len(self.config['keywords']['english'])} 个关键词")

    def build_arxiv_query(self) -> str:
        """构建 arXiv 查询语句"""
        # 核心关键词组合（避免查询过于宽泛）
        core_terms = [
            "Urban Air Mobility",
            "eVTOL",
            "Vertiport",
            "Advanced Air Mobility"
        ]

        # 构建 OR 查询
        query_parts = []
        for term in core_terms:
            # 同时搜索标题和摘要
            query_parts.append(f'(ti:"{term}" OR abs:"{term}")')

        query = " OR ".join(query_parts)
        return query

    def search_arxiv(self) -> List[Dict[str, Any]]:
        """搜索 arXiv 预印本"""
        print("\n🔍 正在搜索 arXiv...")

        query = self.build_arxiv_query()
        lookback_date = datetime.now() - timedelta(days=self.config['output']['days_lookback'])

        client = arxiv.Client()
        search = arxiv.Search(
            query=query,
            max_results=self.config['output']['max_results_per_source'],
            sort_by=arxiv.SortCriterion.SubmittedDate
        )

        papers = []
        for result in client.results(search):
            # 过滤时间范围
            if result.published.replace(tzinfo=None) < lookback_date:
                continue

            paper_data = {
                "title": result.title,
                "authors": [author.name for author in result.authors],
                "abstract": result.summary.replace('\n', ' '),
                "published": result.published.strftime('%Y-%m-%d'),
                "arxiv_id": result.entry_id.split('/')[-1],
                "pdf_url": result.pdf_url,
                "categories": result.categories,
                "source": "arXiv"
            }
            papers.append(paper_data)

        print(f"   找到 {len(papers)} 篇相关论文")
        return papers

    def search_semantic_scholar(self) -> List[Dict[str, Any]]:
        """搜索 Semantic Scholar（通过 API）"""
        print("\n🔍 正在搜索 Semantic Scholar...")

        # Semantic Scholar API
        base_url = "https://api.semanticscholar.org/graph/v1/paper/search"

        # 使用核心关键词组合查询
        keywords = [
            "Urban Air Mobility eVTOL",
            "Vertiport charging infrastructure",
            "Transportation energy coupling UAM"
        ]

        papers = []
        for keyword in keywords:
            params = {
                "query": keyword,
                "limit": 10,
                "fields": "title,authors,abstract,year,publicationDate,externalIds,url",
                "publicationDateOrYear": f"{datetime.now().year - 1}-"  # 最近 1 年
            }

            try:
                response = requests.get(base_url, params=params, timeout=10)
                response.raise_for_status()
                data = response.json()

                for paper in data.get('data', []):
                    paper_data = {
                        "title": paper.get('title', 'N/A'),
                        "authors": [a.get('name', 'Unknown') for a in paper.get('authors', [])],
                        "abstract": paper.get('abstract', 'No abstract available'),
                        "published": paper.get('publicationDate', paper.get('year', 'N/A')),
                        "doi": paper.get('externalIds', {}).get('DOI'),
                        "arxiv_id": paper.get('externalIds', {}).get('ArXiv'),
                        "url": paper.get('url'),
                        "source": "Semantic Scholar"
                    }
                    papers.append(paper_data)

                time.sleep(1)  # API 限速

            except Exception as e:
                print(f"   ⚠️  查询失败 [{keyword}]: {e}")
                continue

        # 去重（基于标题）
        unique_papers = []
        seen_titles = set()
        for paper in papers:
            title_normalized = paper['title'].lower().strip()
            if title_normalized not in seen_titles:
                seen_titles.add(title_normalized)
                unique_papers.append(paper)

        print(f"   找到 {len(unique_papers)} 篇相关论文")
        return unique_papers

    def generate_markdown_summary(self) -> str:
        """生成 Markdown 格式的每日汇总"""
        today = datetime.now().strftime('%Y-%m-%d')

        md_lines = [
            f"---",
            f"created: {today}",
            f"tags: [type/文献追踪, status/待处理]",
            f"---",
            f"",
            f"# 📚 论文追踪日报 - {today}",
            f"",
            f"## 📊 汇总统计",
            f"",
            f"- arXiv: {len(self.results['arxiv'])} 篇",
            f"- Semantic Scholar: {len(self.results['semantic_scholar'])} 篇",
            f"- **总计**: {self.results['metadata']['total_papers']} 篇",
            f"",
            f"---",
            f""
        ]

        # arXiv 部分
        if self.results['arxiv']:
            md_lines.extend([
                "## 🔬 arXiv 预印本",
                ""
            ])
            for i, paper in enumerate(self.results['arxiv'], 1):
                md_lines.extend([
                    f"### {i}. {paper['title']}",
                    f"",
                    f"- **作者**: {', '.join(paper['authors'][:3])}{'等' if len(paper['authors']) > 3 else ''}",
                    f"- **发表日期**: {paper['published']}",
                    f"- **arXiv ID**: `{paper['arxiv_id']}`",
                    f"- **类别**: {', '.join(paper['categories'])}",
                    f"- **PDF**: [下载]({paper['pdf_url']})",
                    f"",
                    f"**摘要**：",
                    f"> {paper['abstract'][:300]}...",
                    f"",
                    f"---",
                    f""
                ])

        # Semantic Scholar 部分
        if self.results['semantic_scholar']:
            md_lines.extend([
                "## 🎓 Semantic Scholar 发现",
                ""
            ])
            for i, paper in enumerate(self.results['semantic_scholar'], 1):
                md_lines.extend([
                    f"### {i}. {paper['title']}",
                    f"",
                    f"- **作者**: {', '.join(paper['authors'][:3])}{'等' if len(paper['authors']) > 3 else ''}",
                    f"- **发表日期**: {paper['published']}",
                ])

                if paper.get('doi'):
                    md_lines.append(f"- **DOI**: {paper['doi']}")
                if paper.get('arxiv_id'):
                    md_lines.append(f"- **arXiv ID**: `{paper['arxiv_id']}`")
                if paper.get('url'):
                    md_lines.append(f"- **链接**: [查看]({paper['url']})")

                md_lines.extend([
                    f"",
                    f"**摘要**：",
                    f"> {paper['abstract'][:300] if paper['abstract'] else '暂无摘要'}...",
                    f"",
                    f"---",
                    f""
                ])

        # 下一步行动
        md_lines.extend([
            "## 💡 下一步行动",
            "",
            "- [ ] 浏览标题，标记感兴趣的论文",
            "- [ ] 下载 PDF 到 Zotero",
            "- [ ] 调用 `/process-literature` 处理重点文献",
            "",
            f"*本报告由自动化脚本生成于 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*"
        ])

        return "\n".join(md_lines)

    def save_results(self):
        """保存结果到文件"""
        # 1. 保存 JSON 原始数据
        json_path = Path("paper_tracker_results.json")
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, ensure_ascii=False, indent=2)
        print(f"\n✅ 原始数据已保存: {json_path}")

        # 2. 生成 Markdown 日报
        md_content = self.generate_markdown_summary()
        today = datetime.now().strftime('%Y-%m-%d')

        # 使用绝对路径：从脚本所在目录向上定位知识库根目录
        script_dir = Path(__file__).parent.resolve()
        kb_root = script_dir.parent.parent.parent  # _tools -> 城市低空资源研究 -> 04_Projects -> 知识库根目录
        inbox_relative = self.config['output']['inbox_folder'].lstrip('./')
        md_path = kb_root / inbox_relative / f"{today}-论文追踪日报.md"
        md_path.parent.mkdir(parents=True, exist_ok=True)

        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"✅ Markdown 日报已保存: {md_path}")

    def run(self):
        """执行完整的追踪流程"""
        print("=" * 60)
        print("🚀 论文追踪系统启动")
        print("=" * 60)

        # 1. 搜索 arXiv
        self.results['arxiv'] = self.search_arxiv()

        # 2. 搜索 Semantic Scholar
        self.results['semantic_scholar'] = self.search_semantic_scholar()

        # 3. 统计总数
        self.results['metadata']['total_papers'] = (
            len(self.results['arxiv']) +
            len(self.results['semantic_scholar'])
        )

        # 4. 保存结果
        self.save_results()

        print("\n" + "=" * 60)
        print(f"✨ 追踪完成！共发现 {self.results['metadata']['total_papers']} 篇论文")
        print("=" * 60)


def main():
    """主函数"""
    tracker = PaperTracker()
    tracker.run()


if __name__ == "__main__":
    main()
