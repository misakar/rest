rest:decorators: paginate
===

## @paginate 装饰器
分页装饰器

### 参数
+ @paginate(Model, per_page)
    + Model: 被分页的资源对应的数据库Model
    + per_page: 平均每页的资源数

### 使用

    from rest.decorators import paginate

    per_page = current_app.config['PROJECT_PER_PAGE']
    @api.route('/users/', methods=['GET'])
    @paginate(User, per_page)
    def get_users():
        pass

### 备注
@paginate 装饰器遵循最新的API分页标准, 在头部定义link
详见:http://tools.ietf.org/html/rfc5988

