// mockjs --> 生成虚拟数据

var Mock = require('mockjs');
var data = Mock.mock({
    'list|1-10': [{
        'id|+1': 1
    }]
});

console.log(JSON.stringify(data, null, 4));
