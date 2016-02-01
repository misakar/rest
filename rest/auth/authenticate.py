# coding:utf-8
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app


class AuthUser(object):
    """用户验证类"""
    def generate_auth_token(self, expiration):
        """generate a token"""
        s = Serializer(
            current_app.config['SECRET_KEY'],
            expiration
        )
        return s.dumps({'id': self.id})

    @classmethod
    def verify_auth_token(Model, token):
        """verify the user with token"""
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return Model.query.get_or_404(data['id'])

