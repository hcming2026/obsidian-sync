# 07_Literature — 科研文献库

> 本目录是 **Zotero → Obsidian** 文献笔记的落点,由 `obsidian-zotero-desktop-connector` 插件按
> `07_Literature/{{citekey}}.md` 规则自动生成,请勿手动改动文件命名约定。

## 目录约定

| 内容 | 位置 | 说明 |
| --- | --- | --- |
| 论文笔记 | `07_Literature/<citekey>.md` | 由 Zotero 导入/手动创建,文件名 = 文献引用键(citekey) |
| 批注截图 | `07_Literature/ZoteroImages/<citekey>/` | PDF 批注导入时自动生成 |

## 工作流(文献 → 笔记)

1. **Zotero**:安装 [Better BibTeX](https://retorque.re/zotero-better-bibtex/),收集文献、标注 PDF。
2. **导入**:在 Zotero 中选中条目 → 右键 "Import"(由插件在 Obsidian 侧生成 Markdown 笔记)。
3. **精读**:把导入的文献笔记升华为原子化笔记,链接进 `03_Knowledge/` 对应领域,并挂上 MOC。
4. **引用**:正文中用 `[[citekey]]` 双向链接回文献笔记,形成"观点 → 出处"的可追溯链。

## 注意

- 只同步 Markdown 笔记,**PDF 本体留在 Zotero 本地/同步盘**中,不进 GitHub。
- 引用键格式依赖 Better BibTeX 的 citekey 规则,改动会破坏既有链接,请保持稳定。
