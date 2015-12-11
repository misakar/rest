[rest] a simple API framework for flask
===

![rest](http://7xj431.com1.z0.glb.clouddn.com/i_need_rest_by_gada_chan-d34h65n.jpg) <br/>

    rest是一个flask API框架, 帮助flask开发者快速处理http基础验证,简化API编写,
    同时基于mockjs格式的接口文档一键生成虚拟数据,方便前后端在分离模式下的合作开发

## Hello rest, 从Token开始!
### Token

    token 是包含用户认证信息的一个签名,
    通过token可以安全的使用HTTPBasicAuth验证, 避免敏感信息的泄漏。

    rest框架生成的token基于itsdangeours的JWS(TimedJSONWebSignatureSerializer)模块。
    使用rest框架，几乎不用编写任何代码, 仅需3步即可创建并获取token

### step1: 继承AuthUser类
在models.py中导入AuthUser类, 在User类中继承

    from rest.auth import AuthUser

    class User(db.Model, AuthUser):
        pass

### step2: 构建(初始化)API蓝图
使用rest的api命令轻松构建和初始化API蓝图, 进入蓝图目录:

    $ api init
    \_ api_name [api]:
    \_ auth_field [username]:
    \_ token_time [3600s]:

    api init done !

api_name 就是你的api蓝图的名字, 默认是api,当然你可以加上版本号<br/>
auth_field 是你处理验证的字段名称，比如用户名或者邮箱 <br/>
token_time 是token的寿命,默认是一个小时(3600s) <br/>
然后注册api蓝图

    from api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1.0')


### step3: 获取token
启动你的flask应用

    在请求头中加上用户验证 访问 http://127.0.0.1:5000/api/v1.0/token/
    即可获取token !

httpie测试
![token](http://7xj431.com1.z0.glb.clouddn.com/g)


## rest 框架的更多特性
[🍺 __ 装饰器](https://github.com/neo1218/rest/blob/master/doc%2Fdecorate.md) : 使用装饰器简化你的代码 <br/>
    - @paginate 分页装饰器

[😊 __ 前后端合作](https://github.com/neo1218/rest/blob/master/doc%2Fmock.md) : mockjs 接口文档一键生成后端虚拟数据库数据

## 安装
目前rest还在开发中, 可以使用源码安装rest

    $ git clone https://github.com/neo1218/rest.git
    $ cd rest
    $ sudo pip install .

如果在终端输入 api

    $ api

出现帮助信息, 则rest安装成功
