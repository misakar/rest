# coding: utf-8
# 模块导入(略)
......


class User(db.Model):
    __tablename__ == "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    def __repr__(self):
        return "<User %r>" % self.name
