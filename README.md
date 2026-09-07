# Obsidian 科研知识库(obsidian-sync)

个人科研知识库,采用 **Obsidian + GitHub + Zotero** 三件套工作流:

- **Obsidian** — Markdown 笔记与知识网络(双向链接 + 图谱 + MOC)
- **GitHub(本仓库)** — 私有远程仓库,经 `obsidian-git` 插件自动备份与多端同步
- **Zotero** — 文献管理(收集、PDF 标注),经 `obsidian-zotero-desktop-connector` 将文献笔记导入 Obsidian

> 仓库管理规则见 [CLAUDE.md](./CLAUDE.md),运行命令见 [COMMANDS.md](./COMMANDS.md),规模与索引见 [INDEX.md](./INDEX.md)。

## 目录结构

| 目录 | 用途 | 入库规则 |
| --- | --- | --- |
| `00_Inbox/` | 收集箱,未处理信息 | 临时存放,定期处理归档 |
| `01_Daily/` | 每日笔记 | 日记/复盘/待办,按日期归档 |
| `02_Reading/` | 阅读笔记 | 书籍、网页等非论文阅读 |
| `03_Knowledge/` | 主题知识 | 原子化笔记(一篇一概念),AI 主工作区 |
| `04_Projects/` | 项目资料 | 论文/课题项目文档与输出 |
| `05_Templates/` | 模板库 | 日报、阅读、**文献阅读**等模板 |
| `06_Assets/` | 附件资源 | 图片等媒体 |
| `07_Literature/` | **科研文献库** | Zotero 导入的论文笔记,按 `{{citekey}}.md` 命名 |

## 科研工作流

```
Zotero 收集文献/标注 PDF
      │  (插件: Import Paper)
      ▼
07_Literature/<citekey>.md   ← 文献笔记落点
      │  (精读提炼)
      ▼
03_Knowledge/ 原子化笔记 + [[citekey]] 溯源链接 + MOC 主题地图
      │  (obsidian-git 每 5 分钟)
      ▼
GitHub 私有仓库(obsidian-sync)  ← 跨设备自动同步/备份
```

要点:

1. **引用溯源**:任何笔记中的观点若来自某篇论文,用 `[[citekey]]` 链接回 `07_Literature/` 下的文献笔记,保证"观点 → 出处"可追溯。
2. **PDF 不进仓库**:论文 PDF 本体放在 Zotero 中,本仓库只同步 Markdown 与轻量图片。
3. **文献读后即拆**:精读完的文献,把可复用的方法/结论拆成原子化笔记挂进对应领域,而不是让文献笔记堆在 `07_Literature/` 里吃灰。

## 插件清单

| 插件 | 作用 |
| --- | --- |
| [obsidian-git](https://github.com/Vinzent03/obsidian-git) | 自动 commit + push/pull,每 5 分钟备份 |
| [obsidian-zotero-desktop-connector](https://github.com/aidenlx/obsidian-zotero-desktop-connector) | 从 Zotero 导入文献笔记/批注 |

> 本仓库共享插件**配置**(`.obsidian/plugins/*/data.json`)与核心设置(`app.json` 等),不包含插件程序本体——新设备克隆后,在 Obsidian 社区市场重新安装同名插件即可自动套用配置。

## 在新设备上使用(克隆即用)

1. 安装 [Obsidian](https://obsidian.md/),以「打开文件夹作为仓库」打开本目录;
2. 在 Obsidian 设置 → 第三方插件 → 关闭安全模式,安装上面两个插件;
3. 插件会自动读取共享配置;`obsidian-git` 需要 `git` 命令可用,并完成一次 GitHub 凭据认证;
4. (可选)Zotero 端安装 [Better BibTeX](https://retorque.re/zotero-better-bibtex/),保持引用键稳定。

## 同步说明

- 本仓库为 **Private 私有仓库**,仅自己可见。
- 自动提交信息形如 `vault backup: YYYY-MM-DD HH:mm:ss`。
- 每次手动大改后,建议先 `git pull` 再改(obsidian-git 默认 `pullBeforePush` 已开启)。
