rest:cli: api
===
api是rest库提供的命令行工具

## Usage
构建API蓝图, 集成token验证

### step 1. 构建API蓝图
使用<code>api init</code>构建API蓝图

    $ api init
    \_api_name: [api]:
    \_auth_field: [username]:
    \_token_time(s): [3600]:

api_name是api蓝图的名称默认是api <br/>
auth_field是验证字段，比如用户名或者email, 默认是用户名和密码验证<br/>
token_time是token的寿命, 默认是3600s <br/>

### step 2. 注册API蓝图

    from api import api
    app.register_blueprint(api, url_prefix='api')

### step 3. 继承AuthUser类

    from rest.auth import AuthUser

    class User(db.Model, UserMixin, AuthUser):
        pass

### step 4. 创建is_admin()方法
需在User类实现is_admin方法从而判断用户是否具备管理员权限,
如果使用mana构建项目则已经实现了is_admin方法。

