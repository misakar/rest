rest: decorators: permission_required
===
token权限装饰器

## 参数
+ @permission_required(Model, permission)
    + Model: 用户类
    + permission: 具体权限

## 使用

    from rest.decorators import permission_required
    from app.models import User, Permission


    @api.route('/users/<int:id>/', methods=['GET', 'DELETE'])
    @permission_required(User, Permission.DELETE)
    def delete_id_user(id):
        user = User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({
            'delete user': user.id
        })

这样只有具备删除权限的用户可以删除用户, 其余用户删除将返回403错误
