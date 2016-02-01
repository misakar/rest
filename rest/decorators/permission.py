# coding: utf-8
"""
    permission_required
    ~~~~~~~~~~~~~~~~~~~

        token权限装饰器

"""

from functools import wraps
from flask import request


def permission_required(Model, permission):
    def permission_decorator(f):
        @wraps(f)
        def decorator(*args, **kwargs):
            token_header = request.headers.get('authorization')
            token = token_header[6:]
            if token:
                user = Model.verify_auth_token(token)
                if user.can(permission):
                    return f(*args, **kwargs)
                else:
                    abort(403)
            else:
                abort(403)
        return decorator
    return admin_decorator

