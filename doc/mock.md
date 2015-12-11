rest 框架文档 mock
===
![mockjs](http://7xj431.com1.z0.glb.clouddn.com/9.08.54.png)

## Mockjs
[官网](http://mockjs.com/)

    Mock.js
    是一款模拟数据生成器，旨在帮助前端攻城师独立于后端进行开发，帮助编写单元测试。提供了以下模拟功能
    {
        根据数据模板生成模拟数据
        模拟 Ajax 请求，生成并返回模拟数据
        基于 HTML 模板生成模拟数据
    }
    可以使用npm安装: npm install mockjs

## 基于mockjs的前后端分离开发
有了mockjs, 前后端就可以<strong>并行开发</strong>, 一般流程如下

    1.              确定API接口,数据模版,命名规范
                    |                          |
    2. 前端使用mock模版生成虚拟数据      后台进行API开发
                    \______________|__________/
    3.                       前端撤掉虚拟数据
                                前后端合并

## 后台虚拟数据问题

    后台在进行API开发的时候也需要面对生成虚拟数据库数据的问题, 传统的生成方式有
    forgery_py(https://github.com/tomekwojcik/ForgeryPy),但是个人使用感觉forgery_py依据模版
    生成的数据过于"静态化", 无法很好的模拟数据与数据之间的关系,即SQL数据库里的"外键"关系


## rest 框架的mock命令: 使用mock生成后台虚拟数据

    rest框架提供mock命令,通过API的方式将mock模版生成的json数据导入数据库从而生成虚拟数据, 由于mockjs具有随机
    灵活的特性, 所以可以比较好的模拟数据之间的关系。
    此外, 前后端使用一套mockjs模版,更加方便日后的前后端合并,减少合并时的字段命名、数据的冲突


## 使用rest框架的mock命令
以[User类](https://github.com/neo1218/rest/blob/master/doc%2Fcode%2FUser.py)为例<br/>
### 1. 编写mockjs模版

    使用api命令构建api蓝图会自动在api蓝图中生成mock/gen_data.js文件(gen_data.js即为模版文件)

打开 gen_data.js 文件:

    // mockjs
    // doc url: http://mockjs.com/

    var Mock = require('mockjs');
    var data = Mock.mock({
        "lists|20": [{
            "id|+1": 1,
            "name": "neo1218"
        }]
    });

    console.log(JSON.stringify(data, null, 4));

### 2. 在终端生成json文件(gen_data.json)

    $ node gen_data.js > gen_data.json

### 3. 生成虚拟数据
在api蓝图所在的目录执行

    $ mock api
    \__ Model:

Model 就是你希望生成虚拟数据的数据库Model <br/>
返回信息:
![201](http://7xj431.com1.z0.glb.clouddn.com/9.43.08.png)
