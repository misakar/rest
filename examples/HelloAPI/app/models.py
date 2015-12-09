# coding: utf-8
"""
    models.py
    ~~~~~~~~~

        数据库文件
"""
from . import db


class Student(db.Model):
    """
    the student class
    """
    id = db.Column(db.Integer, primary_key=True)
