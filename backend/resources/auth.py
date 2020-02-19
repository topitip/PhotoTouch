import falcon
import hashlib

from libs.auth import (
    make_session, auth_required,
    config, remove_session
)
from schemas.user import (
    LoginSchema, RegisterSchema,
    UserUpdateSchema, UserPublicSchema
)
from libs.decorators import with_body_params
from models.user import User



class CurrentUserController(object):

    def __init__(self):
        self.user = None

    @falcon.before(auth_required)
    def on_get(self, req, resp):

        resp.body = UserPublicSchema().dumps(self.user)


class UserLoginController(object):

    @with_body_params(LoginSchema)
    def on_post(self, req, resp):

        phone = req.parsed['phone']
        password = req.parsed['password']+config['secure']['salt_password']

        try:
            user = (
                User
                .select(User.id)
                .where(User.phone == phone)
                .where(
                    User.password == hashlib.sha256
                    (password.encode())
                    .hexdigest()
                )
                .get()
            )
        except Exception:
            raise falcon.HTTPUnauthorized()

        try:
            resp.set_cookie(
                'user_session',
                make_session(
                    credential=phone,
                    user_data=req.host+req.user_agent,
                    user_id=user.id
                ),
                path='/'
            )
        except Exception:
            raise falcon.HTTPUnauthorized()


class RegistrationController(object):

    @with_body_params(RegisterSchema)
    def on_post(self, req, resp):
        user = User(**req.parsed)

        password = req.parsed['password']+config['secure']['salt_password']
        user.password = hashlib.sha256(password.encode()).hexdigest()

        try:
            user.save()
        except Exception:
            raise falcon.HTTPUnprocessableEntity()

        try:
            resp.set_cookie(
                'user_session',
                make_session(
                    credential=user.phone,
                    user_data=req.host+req.user_agent,
                    user_id=user.id
                ),
                path='/'
            )
        except Exception:
            raise falcon.HTTPUnauthorized()


class LogoutController(object):

    @falcon.before(auth_required)
    def on_post(self, req, resp):

        remove_session(req.cookies['user_session'])
