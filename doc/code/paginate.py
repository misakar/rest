# coding: utf-8
# 模块导入(省略)
......

"""
传统的flask分页
"""
@api.route('/users/', methods=['GET'])
def get_users():
    page = request.args.get('page', 1, type=int)
    pagination = User.paginate(
        page,
        per_page=current_app.config['PAGINATION_CONFIG'],
        error_out=False
    )
    users = pagination.items
    prev = ""
    if pagination.has_prev:
        prev = url_for('api.get_users', page=page - 1, _external=True)
    next = ""
    if pagination.has_next:
        next = url_for('api.get_users', page=page + 1, _external=True)
    users_count = len(User.query.all())
    if users_count % current_app.config["PAGINATION_CONFIG"] == 0:
        page_count = users_count//current_app.config["PAGINATION_CONFIG"]
    else:
        page_count = users_count//current_app.config["PAGINATION_CONFIG"] + 1
    last = url_for('api.get_users',  page=page_count, _external=True)
    return json.dumps(
        [user.to_json() for user in users],
        ensure_ascii=False,
        indent=1
    ), 200, {'Link': '<%s>; rel="next", <%s>; rel="last"' % (next, last)}


"""
使用pagination装饰器
"""
per_page = current_app.config["PAGINATION_CONFIG"]
@api.route('/users/', methods=['GET'])
@pagination(User, per_page)
def get_users():
    pass
