# 更正与制作范围

## 失落动作

[失落更正记录](corrections/failed-motion-correction.json)优先于历史计划冲突文字。原动作包含屈膝、坐下抱膝、放松手臂、起身恢复，不能简化为低头。完整预算仍37帧；候选来源不等于完整验收。

## 接触点校正

允许在保留原稿的前提下，对导出副本做有限接触位置校正与统一导出，记录参数和实测误差。不得用局部变形掩盖身份、头身比例、服饰和翼骨错误；不得凭空合成未生成姿态冒充画稿。

## 路径与状态

plans内file/sourceFile为未来生产目标，并不意味着对应成品已存在。实际候选文件由assets/catalog.json和groups内current-timeline.json索引。catalog路径相对仓库根；timeline的file相对本动作组目录。

reference/auxiliary-coverage.json中33项有候选来源，3项程序校准图尚无来源，不要求网页把它们生成成带标线的角色成品。辅助图也不是全部正式美术验收通过。

qa中的来源标识与本地生产相对路径用于溯源；实际公开图片通过catalog的id查找。公开材料不包含废稿、被替换母版或私人工作会话。
