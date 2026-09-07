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

## 在新设备上使用（克隆即用）

1. 安装 [Obsidian](https://obsidian.md/),在终端执行(需先配置好 GitHub 凭据):

   ```bash
   git clone https://github.com/hcming2026/obsidian-sync.git
   cd obsidian-sync
   ```

2. 在 Obsidian 里选择「打开文件夹作为仓库」,指向 `obsidian-sync` 目录;
3. 设置 → 第三方插件 → 关闭安全模式 → 浏览安装 `obsidian-git` 与 `obsidian-zotero-desktop-connector`;
4. 插件会自动读取仓库里共享的配置(`.obsidian/plugins/*/data.json`),无需重新设置;
5. (可选)Zotero 端安装 [Better BibTeX](https://retorque.re/zotero-better-bibtex/),保持引用键稳定。

## 如何同步（实操指南）

### 1. 同步原理

仓库根目录已配置好 Git 远程(私有仓库 `hcming2026/obsidian-sync`),并由 **obsidian-git** 插件定时执行:

- 每 **5 分钟**自动 `commit`(提交信息形如 `vault backup: YYYY-MM-DD HH:mm:ss`);
- 提交后自动 `push` 到 GitHub;`push` 前会先 `pull`(合并云端最新改动),避免多端冲突;
- 本仓库已随库同步插件配置,所有设备克隆后行为一致。

### 2. 日常无需手动操作

只要保证 **Obsidian 处于打开状态**,改动笔记后最多等 5 分钟,云端即已更新。可开启「状态栏图标」,悬停可看到上次备份时间。

### 3. 想立即同步（手动触发）

按 `Ctrl+P` 打开命令面板,输入并执行:

- `Obsidian Git: Push` —— 提交并推送本地改动;
- `Obsidian Git: Pull` —— 拉取云端最新改动;
- `Obsidian Git: Push and Sync`(或 `Backup`)—— 先拉后推,一步完成。

> 建议每次手动大改后执行一次 `Push`(plugin 默认已开启 pull-before-push,无需担心覆盖云端)。

### 4. 在新设备上首次使用

克隆并打开仓库后,在 obsidian-git 设置中勾选 **`Auto pull on startup`**(默认关闭,首台设备建议开启),这样每次打开 Obsidian 都会自动拉取最新;然后手动执行一次 `Obsidian Git: Pull` 确认能连通远程。

### 5. 常见问题

| 现象 | 解决方法 |
| --- | --- |
| Push 时报 `could not read Username` / 401 | 本机未保存 GitHub 凭据。先安装 [Git for Windows](https://git-scm.com/) 并在任意终端执行一次 `git push` 完成登录(推荐 HTTPS + 凭据管理器),Obsidian 内即可复用 |
| 报 `CONNECT tunnel failed` / 网络超时 | 公司/校园网代理导致,在 Git 中配置代理或切换网络后重试 |
| `Auto pull` 冲突弹窗 | 两台设备同时改同一笔记所致。手动合并冲突后提交,或放弃本地改动(命令 `Obsidian Git: Discard` 谨慎使用) |
| obsidian-git 提示找不到 git | 在插件设置 → 高级里手动指定 git 可执行文件路径(Windows 一般为 `C:\Program Files\Git\bin\git.exe`) |

### 6. 备份纪律

- 本仓库是**私有**的,但仍建议重要论文/课题另做一份本地压缩备份;
- 论文 PDF 本体在 Zotero 中管理,不依赖本仓库;
- 若误删笔记,可在 Obsidian 文件恢复(需插件)或 GitHub 提交历史中找回。
