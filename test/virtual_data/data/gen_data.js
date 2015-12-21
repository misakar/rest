// mockjs --> 生成虚拟数据

va Mock = require('mockjs');
var data = Mock.mock({
    "lists|20": [{
        "id|+1": 1,
        "name": "haha"
    }]
});

console.log(JSON.stringify(data, null, 4));
