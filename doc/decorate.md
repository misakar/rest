rest 框架文档: 装饰器
===
![do not repeat yourself](http://7xj431.com1.z0.glb.clouddn.com/10.30.24.png)

    rest 框架使用装饰器简化重复代码的编写,这篇文档将介绍rest框架中的装饰器
    以及如何使用这些装饰器,以下所有的装饰器都可以从rest.decorators命名空间中导入

## @paginate 分页装饰器

    flask的分页处理麻烦且重复, 使用分页装饰器是一个好的办法

[flask分页与使用分页装饰器对比](https://github.com/neo1218/rest/blob/master/doc%2Fcode%2Fpaginate.py)
#### @paginate(Model, per_page)
<strong>Model:</strong> 资源类 <br/>
<strong>per_page:</strong> 每页的数据量 <br/>
在使用paginate装饰器之前需要在相应类中实现<strong>to_json()</strong>方法<br/>

httpie测试:
![分页](http://7xj431.com1.z0.glb.clouddn.com/1111png)

@paginate 装饰器遵循最新的API分页标准, 在头部定义link
详见:http://tools.ietf.org/html/rfc5988
