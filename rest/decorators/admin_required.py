# coding: utf-8
'''
    admin_required.py
    ~~~~~~~~~~~~~~~~~

        token权限管理装饰器
'''

from functools import wraps
from flask import request


def admin_required(UserModel, f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token_header = request.headers.get('authorization')
        token = token_header[6:]
        if token:
            user = UserModel.verify_auth_token(token)
            if user.is_admin():
                return f(*args, **kwargs)
            else:
                abort(403)
        else:
            abort(403)
    return decorator

