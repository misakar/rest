rest: decorators: admin_required
===
token管理员权限装饰器

## 参数
+ @admin_required(Model)
    + Model: 用户类

## 使用

    from rest.decorators import admin_required
    from app.models import User

    @api.route('/users/<int:id>/', methods=['GET', 'DELETE'])
    @admin_required(User)
    def delete_id_user(id):
        user = User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({
            'delete user': user.id
        })

这样只有管理员可以删除用户, 其余用户删除将返回403错误
