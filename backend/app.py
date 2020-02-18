import falcon

from libs.peewee import PeeweeMiddleware
from routing import make_route


app = falcon.API(
    middleware=[PeeweeMiddleware()]
)

app.resp_options.secure_cookies_by_default = False

make_route(app)
