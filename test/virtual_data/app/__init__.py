# coding: utf-8
"""

    ~~~~~~~

"""

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import config


app = Flask(__name__)


app.config.from_object(config['default'])


db = SQLAlchemy(app)


from api import api as api_1_0
app.register_blueprint(api_1_0, url_prefix='/api/v1.0')


from . import views, models, forms
