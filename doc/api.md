rest API doc
===

## Authentication
### HTTPBasicAuthentication
#### :class AuthUser:
<strong> :func generate_auth_token(): </strong>

    this is the function to generate user token for
    HTTPBasicAuthentication

<strong> :func verify_auth_token(): </strong>

    this function can verify user token to get user id

#### :cli api:
api command can auto create api blueprint and init HTTPBasicAuthentication
(you need to make your User model inhert class AuthUser)
then:

    cd the folder you want to create restful api,
    and type:

    $ auth init
    \_ api_name: api
    \_ token_time(s): 3600*24

    [info] HttpBasicAuth init done...!

and now you have:

    app--api--__init__.py (api blueprint and you just need regist it on
    app)    |
            --authentication.py (HTTPBasicAuthentication use jws token)

## Decorators
#### @json

    @json decorators can jsonify the response value(rv)

#### @login_required

    decorator @login_required can add a login authentication to a view function

#### @rate_limit(max=.., per=..)

    @rate_limit can limit the request from same ip

#### @cache

    @cache add cache

#### @etags

    @etags add etags

### @paginate

    @paginate pagination

