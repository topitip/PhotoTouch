from resources.index import IndexController
from resources.auth import (
    UserLoginController, RegistrationController,
    LogoutController, CurrentUserController
)


def make_route(app):

    app.add_route('/', IndexController())
    app.add_route('/login', UserLoginController())
    app.add_route('/signup', RegistrationController())
    app.add_route('/logout', LogoutController())
    app.add_route('/users/current', CurrentUserController())
