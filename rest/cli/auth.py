# coding: utf-8

"""
    rest auth cli
    ~~~~~~~~~~~~~

        auth init api --time=3600*24
"""

import click
import os
import sys

# path
project_path = os.path.abspath(os.path.join(os.path.dirname("__file__"), '..'))
if project_path not in sys.path:
    sys.path.insert(0, project_path)

# logging
import logging
from logging import StreamHandler, DEBUG
logger = logging.getLogger('__name__')
logger.setLevel(DEBUG)
console = StreamHandler()
logger.addHandler(console)


@click.group()
def cli():
    """rest auth cli"""
    pass


@click.command()
@click.argument('api_blueprint_name')
@click.option('--time', default=False, help="the expiration time of token")
def init(api_blueprint_name):
    """
    rest auth cli

    :example:
        from rest.auth import AuthUser
        class User(AuthUser):
            pass
        $ auth init api_blueprint_name --time=3600*24
        (default time is 3600s)

    :param api_blueprint_name:
        the name of api blueprint
    :return:
        None
    """
