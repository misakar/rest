HelloAPI
===

    这是一个简单的提供API服务的flask小项目

## 1. 使用mana构建工程

    $ mana startproject HelloAPI
    $ virtualenv venv && pip install -r requirement.txt
    $ python manage.py db init/ migrate/ upgrade
    $ python manage.py admin

具体使用见[mana](https://github.com/neo1218/mana)

## 2. 提供API服务
### API文档:
这个小项目主要提供**用户CRUD**API<br/>

1. *获取所有用户信息*
    + **API**: /api/users/?page=1&&per_page=10
    + **METHOD**: GET
    + **返回字段(单条数据样例)**:
        + id: Integer
        + username: String
        + email: String

2. *获取特定id用户信息*
    + **API**: /api/users/<int:id>/
    + **METHOD**: GET
    + **返回字段**:
        + id: Integer
        + username: String
        + email: String

3. *创建一个用户*
    + **API** /api/users/
    + **METHOD**: POST
    + **Authorization**: 管理员token
    + **发送json body**:
        + id: Integer
        + username: String
        + email: String
    + **返回信息**:
        + 状态码: 201
        + id: Integer

4. *更新特定的用户信息*
    + **API**: /api/users/<int:id>/
    + **METHOD**: PUT
    + **Authorization**: 管理员token
    + **发送json body**:
        + id: integer
        + username: String
        + email: String
    + **返回信息**:
        + 状态码: 200
        + id: Integer

5. *删除特定的用户*
    + *API*: /api/users/<int:id>/
    + **METHOD**: DELETE
    + **Authorization**: 管理员token

### 编写API服务

1. 使用<code>rest init</code>构建API蓝图, 集成token验证
    1. <code>cd app && rest init</code>, 验证字段为email
    2. 注册API蓝图:
        + <code>from .api import api</code>
        + <code>app.register_blueprint(api, url_prefix='api')</code>
    3. 继承**AuthUser**类
        + <code>from rest.auth import AuthUser</code>

2. 依据文档字段, 创建<code>to_json</code>和<code>from_json</code>方法
    + [to_json()]()
    + [from_json()]() => 搭配<code>request.get_json()</code>使用


3. 编写**获取所有用户信息API**
    + 使用**rest pagenate分页装饰器**, [详细代码]()

4. 编写**获取特定用户信息API**


5. 编写**创建用户API**
    + 使用**rest admin_required装饰器**, [详细代码]()


6. 编写**更新特定用户信息API**
    + 使用**rest admin_required装饰器**, [详细代码]()


7. 编写**删除特定用户API**
    + 使用**rest admin_required装饰器**, [详细代码]()

8. 部署

完成

## 在本地构建这个例子
1. clone example 文件夹
