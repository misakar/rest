HelloAPI
===

    students and there classes

## API
#### /api/v1.0/students/      GET

    return all the student info

    {
        "count": 20
        "data":
        [
            {
                "name": "neo1218",
                "class": 1
            },
            {
                "name": "zxchaha",
                "class": 2
            }
        ]
        "first": /api/v1.0/students/?page=1&per_page=10
        "last": /api/v1.0/students/?page=2&per_page=10
        "prev": null
        "next": /api/v1.0/students/?page=2&per_page=10
    }

#### /api/v1.0/students/<int:id>/  GET
