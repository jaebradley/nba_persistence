from django.core.management.base import BaseCommand

from data.inserters.static import insert_positions, insert_seasons, insert_teams


class Command(BaseCommand):
    def __init__(self, stdout=None, stderr=None, no_color=False):
        super(Command, self).__init__(stdout, stderr, no_color)

    def handle(self, *args, **options):
        Command.insert()

    @staticmethod
    def insert():
        insert_positions()
        insert_seasons()
        insert_teams()
