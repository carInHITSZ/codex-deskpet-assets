# 桌宠控制模式接口与菜单更新

日期：2026-10-19。范围：本地已安装霜序桌宠的行为控制；不修改动画素材生产验收状态。

## 用户要求

允许主动进入、退出待机跟随鼠标状态，以优先级覆盖自动行为，不屏蔽其他手动指令。待机跟随作为默认控制模式，并在右键和托盘菜单提供可见入口。

## 已实现

- 统一名称为“控制模式（Control Mode）”，与短暂的动作Action分开。
- `idle_follow`：待机并跟随鼠标，覆盖Paseo自动状态和随机行为。
- `auto`：退出待机跟随覆盖，恢复Paseo及原有自动行为设置。
- 默认idle_follow；主动选择保存到设置，重启保留。
- 优先级：暂停/隐藏/拖动控制 > 手动动作 > 待机跟随覆盖 > Paseo和随机自动行为。
- 双击挥手、动作菜单和动作接口继续响应；临时动作完成后回到当前控制模式，不自动关闭待机跟随。
- 原自动散步、视线、随机动作设置不因模式切换被强制改写。

## 修正菜单遗漏

早期版本仅完成命令接口，菜单入口未成功插入；已根据用户截图确认并补齐。

右键桌宠或托盘 → **控制模式** → **待机跟随鼠标 / 自动联动 Paseo**。

菜单顶部状态改为当前实际基础状态，避免角色处于待机跟随但菜单仍写“认真工作中”。

## 接口

在桌宠程序目录执行：

```powershell
node pet-control.cjs modes
node pet-control.cjs mode idle_follow
node pet-control.cjs mode auto
node pet-control.cjs status
node pet-control.cjs action waving 1000
```

旧follow命令继续作为idle_follow兼容别名。

Windows本地命名管道：`\\.\pipe\shuangxu-desktop-pet-control`。每连接发送一行JSON并接收一行JSON，无HTTP端口，无任意代码执行接口。

```json
{"command":"mode","mode":"idle_follow"}
```

可用command包括mode、modes、status和action。动作时长限制100–30000ms。模式注册集中于control-modes.cjs；菜单和模式列表共用注册信息。当前仅公布已实现的两个模式，睡眠、散步等额外控制模式尚未实现。

## 实际验证

- JavaScript语法检查通过。
- 本地真实命名管道已验证状态查询、follow兼容命令及auto/idle_follow切换。
- modes返回两个已实现模式及优先级。
- idle_follow→手动挥手→动作结束返回idle_follow已实测。
- 重启后确认idle_follow状态恢复；自动联动测试时可显示Paseo运行状态。
- 菜单条目已在代码中补齐并重启加载；未将代码检查冒充用户原生鼠标点击验收。

## 与素材项目的关系

本次没有新生图，没有将任何候选素材升级为正式验收通过，也不覆盖网页端idle生产PR的进度。高清素材生产继续按既有队列、PR和检查点执行。

实现文件位于本地运行目录：main.cjs、control-modes.cjs、control-server.cjs、pet-control.cjs、CONTROL.md。本次GitHub更新为工作记录，未声称这些运行源码已同步到此素材仓库。
