## 大屏下载器-Android

- 本地信息显示：

  - 本机IP地址
  - 品牌+型号+Android_ID
  - android api版本
  - SN（android10+显示高版本系统无法获取）

- 服务器接口注册：

  - APP调用服务端接口`\v1\api\reg\`发送”品牌+型号+Android_ID“字符串，服务端返回`设备ID`和`点位描述`
  - 在线信息模块显示`设备ID`和`点位描述`，请求不到时，显示”非在线状态“提示

- 下载和安装：

  - APP调用服务端接口`\v1\api\checkupdate\`发送”品牌+型号+Android_ID“，服务端返回`APP_ID`,`APP_name`,`APP_DOWNLOAD_uri`
  - 下拉框可以选择APP_name
  - 点击下载后，会自动下载选择项目的安装包到安卓`\download\toinstall.apk`(如路径下存在改文件则覆盖之)
  - 点击安装按钮后，则自动安装toinstall.apk

- 基础功能
  - 使用Kotlin + jetpack compose
  - retrofit：放开http限制，允许访问所有http服务器
  - 应用启动时，会检查并向用户申请必要权限
  - 标准的MVI架构，代码结构数据源、data layer 、 UI layer
- 安卓客户端调用\v1\api\endpoint\接口 向服务器发送‘”品牌+型号+Android_ID’    `android_api`  服务端解析出请求ip后，返回 终端id（未绑定则空） 客户端id  apk名称 apk下载地址 同时更新设备上线日志表中的ip和上线时间！！



## 大屏下载器-服务端

- 整体描述：一个Django实现的Android客户端管理&客户端Apk分发管理工具
- 数据建模：
  - 终端：`终端id`   `终端code`  `终端描述` `终端位置` `创建日期` 	`是否删除` 
  - 客户端：`客户端id` `客户端标识`（客户端发来的”品牌+型号+Android_ID“字符串）  `创建日期` 	`是否删除` 
  - 客户端上线日志：`客户端id`、`上线客户端ip` `上线时间` 
  - 终端-客户端绑定表：`终端id` `客户端id` `开始日期`  `结束日期`
  - 分发项目：`项目id` `项目描述` `项目包名`
  - 项目apk:`apk_id` `项目id` `上传日期` `apk路径`
  - 终端-apk分发：`终端id`  `apk_id` （一个终端id可以属于多个项目的apk包。但一个项目apk包同时只能绑定一个apk_id）

- 终端基础信息管理：注册/修改/关闭（软删除）终端
- 客户端上线自动注册：apk客户端第一次通过api接口调用后（无”品牌+型号+Android_ID“字符串记录），系统自动注册记录到客户端表格中，在django后台权限都不能编辑这个表，只有管理员可以软删除（关闭）
- 客户端上线日志：每次客户端上线后都需要生成一条记录（`客户端id`、`上线客户端ip` `上线时间`  ·上线时绑定的终端id·），所有用户只读此表，只能在Django Admin后台中查看
- 终端-客户端绑定：在Django Admin后台中为一个终端分配一个客户端，一个终端同时只能分配一个客户端
- 分发项目管理：注册、关闭分发项目
- 项目apk注册：选择分发项目后，上传apk包，服务端接收到apk包后需要校验apk包名是否与项目中记录的包名一致方可生成记录
- apk包通过nginx静态地址对外暴露
- 终端-apk分发：在Django Admin后台中为一个终端分配一个需要发布的apk包记录
- REST API实现 与客户端通信
- docker部署 数据库使用sqlite ， nginx+使用 Uvicorn 和 Gunicorn 部署 Django 应用