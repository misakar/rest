# coding: utf-8
_init_py = '''# coding: utf-8
from flask import Blueprint

%s = Blueprint('%s', __name__)

from . import authentication
'''
