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

# templates
from templates._init_py import _init_py
from templates._auth_py import _auth_py
from templates._mock_js import _mock_js


# click
@click.group()
def cli():
    """rest auth cli"""
    pass


@click.command()
# @click.argument('api_name')
# @click.argument('token_time')
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
        \_ auth_field: email
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
    api_name = click.prompt('\_ api_name: ', default='api')
    auth_field = click.prompt('\_ auth_field: ', default='username')
    token_time = click.prompt('\_ token_time(s): ', type=int, default=3600)

    if not api_name:
        logger.warning("api name can't be empty!")
        return

    if not auth_field:
        logger.warning("auth field can't be empty")
        return

    if not token_time:
        logger.warning("token expiration can't be empty")
        return

    # api destination path
    dst_path = os.path.join(os.getcwd(), api_name)

    if os.path.isdir(dst_path):
        logger.warning("api blueprint path already exists!\nnot create new api blueprint")
        return

    logger.info("start generate api blueprint and httpbasicauth file...")

    # create project destination path
    _mkdir_p(dst_path)

    # create __init__.py file
    os.chdir(dst_path)
    init_code = _init_py % (api_name, api_name)
    with open("__init__.py", 'w+') as f:
        f.write(init_code)

    logger.info('init file __init__.py...')

    # create authentication file
    init_code = _auth_py % (auth_field, token_time, token_time)
    os.chdir(dst_path)
    with open("authentication.py", 'w+') as f:
        f.write(init_code)

    logger.info('init file authentication.py...')

    # create mock/gen_data.js file
    mock_path = os.path.join(dst_path, 'mock')
    _mkdir_p(mock_path)
    init_code = _mock_js
    os.chdir(mock_path)
    with open("gen_data.js", 'w+') as f:
        f.write(init_code)

    logger.info('init file mock/gen_data.js...')

    logger.info('api init done!')


######################
cli.add_command(init)
######################
