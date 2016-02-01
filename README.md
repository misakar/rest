rest: 基于flask的API库
===

## 基本思想
rest库是对[木犀团队](https://github.com/Muxi-Studio)后端项目的总结。<br/>

- [木犀后端API开发流程](https://github.com/neo1218/rest/blob/master/doc/README.md) <br/>
- [使用flask编写API的核心思想]() <br/>

## 工具文档:
rest 提供了如下几种类型的工具方便API的编写:

- **cli**命令行工具
    - [api](https://github.com/neo1218/rest/blob/master/doc/api.md)
- **decorator**装饰器工具
    - [@paginate](https://github.com/neo1218/rest/blob/master/doc/paginate.md)
    - [@admin_required](https://github.com/neo1218/rest/blob/master/doc/admin.md)
    - [@permission_required](https://github.com/neo1218/rest/blob/master/doc/permission.md)
    - [@auth.login_required](https://github.com/neo1218/rest/blob/master/doc/login.md)

## example:
- 这个flask项目使用mana和rest构建了一个提供基本CRUD API服务的web应用
    - [HelloAPI](https://github.com/neo1218/rest/tree/master/examples)

## 安装rest:
从源码安装, rest只是某个人对API的编写总结, 从源码安装方便大家修改源码，把自己的思想融入进去

    $ git clone https://github.com/neo1218/rest.git
    $ cd rest
    $ pip install (--editable) .

## Thanks:
- 命令行工具使用[click](https://github.com/mitsuhiko/click.git)开发
- 使用装饰器的方式受到[这个视频](https://www.youtube.com/watch?v=px_vg9Far1Y)的启发

## LICENSE
[MIT](https://github.com/neo1218/rest/blob/master/LICENSE)

