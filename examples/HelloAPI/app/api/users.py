# coding: utf-8
"""
    users.py
    ~~~~~~~~

        用户CRUD API操作
"""
from . import api
from flask import jsonify, request
from app.models import User
from rest.decorators import paginate, admin_required
from app import db


@api.route('/users/')
@paginate(User, 10)
def get_users():
    pass


@api.route('/users/<int:id>/')
def get_id_user(id):
    user = User.query.get_or_404(id)
    return jsonify(
        user.to_json()
    )


@api.route('/users/', methods=['GET', 'POST'])
@admin_required(User)
def new_user():
    user = User.from_json(request.get_json())
    db.session.add(user)
    db.session.commit()
    return jsonify({
        'new user': user.id
    }), 201


@api.route('/users/<int:id>/', methods=['GET', 'PUT'])
@admin_required(User)
def update_user(id):
    user = User.query.get_or_404(id)
    user.username = request.get_json().get('username', user.username)
    user.email = request.get_json().get('email', user.email)
    db.session.add(user)
    db.session.commit()
    return jsonify({
        'update user': user.id
    }), 200


@api.route('/users/<int:id>/', methods=['GET', 'DELETE'])
@admin_required(User)
def delete_id_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({
        'delete user': user.id
    })

