#!./env/bin/python3
from sys import exit
from argparse import ArgumentParser
from peewee_migrate import Router

from libs.peewee import database

router = Router(database)

parser = ArgumentParser(description='Peewee migration wrapper')

parser.add_argument('action', metavar='action', type=str,
                    help='migrate / create')

parser.add_argument('name', default=None, metavar='migration name', type=str)

args = parser.parse_args()

if args.action == 'create':
    if args.name:
        try:
            router.create(args.name)
        except Exception:
            print('Can`t create migration "{0}". Exiting'.format(args.name))
            exit(1)
    else:
        ArgumentParser.error()

elif args.action == 'migrate':
    if args.name == 'all':
        try:
            router.run()
        except Exception:
            print('Can`t apply migrations. Exiting')
            exit(1)
    else:
        try:
            router.run(args.name)
        except Exception:
            print('Can`t apply migration "{0}". Exiting'.format(args.name))
            exit(1)
else:
    ArgumentParser.error()
