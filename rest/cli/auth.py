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
def init():
    """
    rest auth cli

    :example:
        from rest.auth import AuthUser
        class User(AuthUser):
            pass

        cd the folder you want to create api
        and type:

        $ api init
        \_ api_name: api
        \_ token_time(s): 3600*24
        [info] api init done...!

        and now you have:
        app--api--__init__.py
                \_authentication.py

    :param api_blueprint_name:
        the name of api blueprint
    :return:
        None
    """
    api_name = raw_input('\_ api_name: \n')
    token_time = int(raw_input('\_ token_time: ')

    if api_name is None:
        logger.warning("api name can't be empty!")

    if toke_time is None:
        logger.warning("token expiration can't be empty")

    # api destination path
    dst_path = os.path.join(os.getcwd(), api_name)

    if os.path.isdir(dst_path):
        logger.warning("api blueprint path already exists!")
        return

    logger.info("start generate api blueprint and httpbasicauth file...")

    # create project destination path
    _mkdir_p(dst_path)


##############
cli.add_command(init)
##############
