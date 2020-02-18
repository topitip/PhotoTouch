import falcon
import hashlib

from config import config
from models.user import User
from libs.redis import Redis


def get_user(user_session):

    user_id = Redis.get(user_session)

    if not user_id:
        raise falcon.HTTPUnauthorized()

    return (
        User
        .select()
        .where(User.id == user_id)
        .get()
    )


def with_auth(req, resp, resource, params):

    if 'user_session' in req.cookies:
        try:
            user = get_user(req.cookies['user_session'])
            resource.user = user
        except Exception:
            resource.user = None        
    else:
        resource.user = None


def auth_required(req, resp, resource, params):

    if 'user_session' not in req.cookies:
        raise falcon.HTTPUnauthorized()

    user = get_user(req.cookies['user_session'])

    if not user:
        raise falcon.HTTPUnauthorized()

    resource.user = user


def user_required(req, resp, resource, params, user_type):

    if 'user_session' not in req.cookies:
        raise falcon.HTTPUnauthorized()

    user = get_user(req.cookies['user_session'])

    if not user or user.type != user_type:
        raise falcon.HTTPForbidden()

    resource.user = user


def make_session(credential, user_data, user_id):

    user_credential = credential+config['secure']['salt_session']+user_data

    session = hashlib.sha256(user_credential.encode()).hexdigest()

    Redis.set(session, user_id)

    return session


def remove_session(session):
    Redis.delete(session)
