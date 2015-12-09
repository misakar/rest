[rest] a simple restfull API framework for flask
===

![rest](http://7xj431.com1.z0.glb.clouddn.com/i_need_rest_by_gada_chan-d34h65n.jpg)

## Hello rest, 从Token开始!
### Token

    token 是包含用户认证信息的一个签名,
    通过token可以安全的使用HTTPBasicAuth验证, 避免敏感信息的泄漏。
    rest框架生成的token基于itsdangeours的JWS(TimedJSONWebSignatureSerializer)模块。

### step1: 继承AuthUser类
在models.py中导入AuthUser类, 在User类中继承

    from rest.auth import AuthUser

    class User(db.Model, AuthUser):
        pass

### step2: 构建(初始化)API蓝图
使用rest的api命令轻松构建和初始化API蓝图, 进入蓝图目录:

    $ api init
    \_ api_name [api]:
    \_ token_time [3600s]:

    api init done !

api_name 就是你的api蓝图的名字, 默认是api,当然你可以加上版本号<br/>
token_time 是token的寿命,默认是一个小时(3600s) <br/>

### step3: 注册API蓝图
和注册其他蓝图一样

    from api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1.0')


### step4: 获取token
启动你的flask应用

    在请求头中加上用户验证 访问 http://127.0.0.1:5000/api/v1.0/token/
    即可获取token !

httpie测试
![token](http://7xj431.com1.z0.glb.clouddn.com/g)


## rest 框架 API 文档

