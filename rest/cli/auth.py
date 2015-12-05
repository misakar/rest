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

# operators
from operators._mkdir_p import _mkdir_p

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

        cd the api blueprint folder

        $ auth init
        \_ api_name: api_1_0
        \_ token_time(s): 3600*24
        [info] HttpBasicAuth init done...!

    :param api_blueprint_name:
        the name of api blueprint
    :return:
        None
    """
    if not api_blueprint_name:
        logger.warning("Api blueprint name can't be empty!")
        return

    # project destination path
    dst_path = os.path.join(os.getcwd(), api_blueprint_name)

    if os.path.isdir(dst_path):
        logger.warning("api blueprint path already exists!")
        return

    logger.info("start generate api blueprint and httpbasicauth file...")

    # create project destination path
    _mkdir_p(dst_path)
