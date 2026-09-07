---
created: 2026-09-07
tags: [知识管理/工作流, type/笔记]
status: 进行中
---

# 科研文献工作流-从Zotero到GitHub

> 对应 `CLAUDE.md`「职责六」与 `README.md`。当你在 Zotero 里读完一篇论文后,按下面的六步把它变成 Obsidian 里的知识,并自动同步到 GitHub。

## 一、六步速查(每篇文献都适用)

| 步骤 | 在哪做 | 做什么 | 产物 |
| --- | --- | --- | --- |
| 1 | Zotero | 打开 PDF 阅读,高亮 + 写批注(批注里写"这能用在哪/哪里存疑") | PDF 批注 |
| 2 | Obsidian | 保持 Zotero 打开,`Ctrl+P` → 执行 **Import notes** | 自动导入 |
| 3 | Obsidian | 打开生成的文件,把批注整理成自己的理解 | `07_Literature/<citekey>.md` |
| 4 | Obsidian | 把可复用的方法/数据拆成原子化笔记,写入 `03_Knowledge/` 对应领域 | 原子化笔记 |
| 5 | Obsidian | 正文用 `[[citekey]]` 链回文献档案页,观点与出处不脱钩 | 溯源链接 |
| 6 | GitHub | 无需操作:obsidian-git 每 5 分钟自动 commit + push;想立即上传则执行 `Obsidian Git: Push` | 云端备份 |

> 原则:**PDF 原件留在 Zotero**,仓库只同步 Markdown;精读后的养分必须拆进 `03_Knowledge/`,文献笔记只作溯源锚点,不要让它越堆越多。

## 二、以 UAM 论文为例的对接清单(待办)

背景:论文《Integrating urban air mobility into the power grid through smart charging solutions》的 PDF 已归档在 `00_Inbox/已处理/`,此前拆出了 4 篇原子化笔记,但**缺少文献档案页**(`07_Literature/<citekey>.md`),4 篇笔记目前无法溯源回原文。

需要对接的 4 篇原子化笔记:

| 现有笔记 | 领域 | 待补动作 |
| --- | --- | --- |
| [[UAM智能充电电网协同框架]] | 交通系统/电网协同 | 正文补 `[[citekey]]`,source 字段标注出处 |
| [[UAM出行需求估计方法]] | 交通系统 | 正文补 `[[citekey]]` |
| [[UAM智能充电对电网福利的提升效果]] | 交通系统 | 正文补 `[[citekey]]` |
| [[机会约束优化处理充电不确定性]] | 交通系统/运筹优化 | 正文补 `[[citekey]]`,并可顺手建一篇关联的运筹优化原子笔记 |

对接步骤(打勾推进):

- [ ] 在 Zotero 中找到该论文条目(可把 `00_Inbox/已处理/` 的 PDF 拖入 Zotero 生成条目),确认已装 Better BibTeX
- [ ] 保持 Zotero 打开,在 Obsidian 执行 `Import notes`,生成 `07_Literature/<citekey>.md`
- [ ] 把真实 citekey 填入上方表格及下面链接占位
- [ ] 为上表 4 篇笔记逐一补上 `[[citekey]]` 溯源链接(可让 Claude Code 执行 `/process-literature` 代劳)
- [ ] 执行 `Obsidian Git: Push`,验证 GitHub 仓库出现 `07_Literature/<citekey>.md`

## 三、相关资源

- 模板:`05_Templates/文献阅读模板.md`(手动精读时复制使用,注意把 `{{citekey}}` 替换为真实引用键)
- 规则:`CLAUDE.md` 职责六(权限边界、索引同步)
- 命令:`.claude/commands/process-literature.md`(批量处理 `07_Literature/` 待拆解文献)
