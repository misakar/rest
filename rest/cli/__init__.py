# coding: utf-8
"""
rest ~ cli

    auth command for auth

    auto generate authentication file for HTTPBasicAuthentication with JWS token

    step1: inherit class AuthUser

        from rest.auth import AuthUser

        class User(db.Model, UserMixin, AuthUser):
            pass

    step2: use auth command to generate authentication file

        auth init api_1_0(the api blueprint name) --time=3600*24
"""

