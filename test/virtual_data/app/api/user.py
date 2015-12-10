# coding: utf-8

from . import api
from flask import request, jsonify
from ..models import User
from .. import db


@api.route('/user/', methods=["POST"])
def new_user():
    """
    创建一个用户
    现在希望批量创建用户
    此时 request.json 就是一个列表的形式
    """
    count = 0
    for user_json in request.json.get('lists'):
        user = User.from_json(user_json)
        db.session.add(user)
        db.session.commit()
        count += 1
    return jsonify({
        "msg": "created user",
        "count": count
    }), 201
