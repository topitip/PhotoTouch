import falcon

from peewee import PostgresqlDatabase

from config import config


database = PostgresqlDatabase(
    config['db'].pop('db'),
    **config['db']
)


class PeeweeMiddleware(object):

    def process_request(self, req, resp):
        database.connect()

    def process_resource(self, req, resp, resource, params):
        resource.db = database

    def process_response(self, req, resp, resource, req_succeeded):
        if not database.is_closed():
            database.close()
