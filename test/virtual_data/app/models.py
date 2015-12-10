# coding: utf-8
"""
    models.py
    ~~~~~~~~~

        数据库文件
"""
from . import db
# from rest import AuthUser


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(60), index=True)

    def to_json(self):
        json_user = {
            "id": self.id,
            "name": self.name
        }
        return json_user

    @staticmethod
    def from_json(request_json):
        id = request_json.get('id')
        name = request_json.get('name')
        return User(
            id = id,
            name = name
        )

    def __repr__(self):
        return "<User %d>" % self.id
