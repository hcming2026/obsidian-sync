---
limit: 100
mapWithTag: false
icon: book-open
tagNames:
filesPaths:
bookmarksGroups:
excludes:
extends:
savedViews: []
favoriteView:
fieldsOrder:
  - st4tus
  - abssts
version: "2.14"
fields:
  - name: status
    type: Select
    options:
      sourceType: ValuesList
      valuesList:
        "1": 未读
        "2": 精读中
        "3": 已精读
        "4": 待复核
      allowNull: false
    path: ""
    id: st4tus
  - name: abstractStatus
    type: Select
    options:
      sourceType: ValuesList
      valuesList:
        "1": 完整
        "2": 片段
        "3": 待补
      allowNull: false
    path: ""
    id: abssts
---
# paper

论文笔记的 FileClass 定义：
- `status`：阅读状态下拉（未读 / 精读中 / 已精读 / 待复核）
- `abstractStatus`：摘要完整度下拉（完整 / 片段 / 待补）
点击属性值即可切换。
