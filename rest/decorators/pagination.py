# coding: utf-8

"""
@pagination 分页装饰器
"""
import functools
from flask import request, url_for
import json


def paginate(Model, per_page):
    """
    :usage:
        per_page = current_app.config["PAGINATION_CONFIG"]
        @api.route('/users/', methods=['GET'])
        @paginate(User, per_page)
        def get_users():
            pass

    :param Model: sql Model class
    :param per_page: : per page
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper():
            page = request.args.get('page', 1, type=int)
            pagination = Model.query.paginate(
                page,
                per_page = per_page,
                error_out = False
            )
            prev = ""
            items = pagination.items
            if pagination.has_prev:
                prev = url_for('api.%s' % func.__name__, page=page - 1, _external=True)
            next = ""
            if pagination.has_next:
                next = url_for('api.%s' % func.__name__, page=page + 1, _external=True)
            items_count = len(Model.query.all())
            if items_count % per_page == 0:
                page_count = items_count//per_page
            else:
                page_count = items_count//per_page + 1
            last = url_for('api.%s' % func.__name__, page=page_count, _external=True)
            func()
            return json.dumps(
                [item.to_json() for item in items],
                ensure_ascii=False,
                indent=1
            ), 200, {'Link': '<%s>; rel="next", <%s>; rel="last"' % (next, last)}
        return wrapper
    return decorator
