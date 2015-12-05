rest
===
a simple python restfull API framework

## API

## Authentication
### HTTPBasicAuthentication
#### :class AuthUser:
<strong> :func generate_auth_token(): </strong>

    this is the function to generate user token for
    HTTPBasicAuthentication

<strong> :func verify_auth_token(): </strong>

    this function can verify user token to get user id

#### :cli auth:
<code>$ auth init api_1_0</code>

    auth command can auto generate authentication.py file for API auth

## Decorators
### @json

    @json decorators can jsonify the response value(rv)

### @login_required

    decorator @login_required can add a login authentication to a view function

### @rate_limit(max=.., per=..)

    @rate_limit can limit the request from same ip

### @cache

    @cache add cache

### @etags

    @etags add etags

### @paginate

    @paginate pagination

## A Full Status Restfull API
