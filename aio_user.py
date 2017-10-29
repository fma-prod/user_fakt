from aiohttp import web

from controller.user import get_user_by_id, get_all_users, create_user, update_user, remove_user
from controller.common import ping


def app_factory(args=()):
    app = web.Application()
    app.router.add_get('/users/', get_all_users, name='all_users')
    app.router.add_get('/users/{id:\d+}', get_user_by_id, name='one_user')
    app.router.add_post('/users/', create_user, name='create_user')
    app.router.add_patch('/users/{id:\d+}', update_user, name='update_user')
    app.router.add_delete('/users/{id:\d+}', remove_user, name='remove_user')

    app.router.add_get('/ping/', ping, name='ping')

    return app