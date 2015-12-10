rest 框架文档: 装饰器
===
![do not repeat yourself](http://7xj431.com1.z0.glb.clouddn.com/10.30.24.png)

    rest 框架使用装饰器简化重复代码的编写,这篇文档将介绍rest框架中的装饰器
    以及如何使用这些装饰器

## @paginate 分页装饰器

    flask的分页处理麻烦且重复, 使用分页装饰器是一个好的办法

[flask分页与使用分页装饰器对比]()
#### @paginate(Model, per_page)
Model: 资源类 <br/>
per_page: 每页的数据量 <br/>
@paginate 装饰器遵循最新的API分页标准, 在头部定义link
详见:http://tools.ietf.org/html/rfc5988
