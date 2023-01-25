"""
Django command to wait for the db untill start
"""

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
import time

from psycopg2 import OperationalError as Psycopg2OpError

"""Django throw error when db is not ready"""


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write(
                    'Database is not availavle, waiting for 1 sec...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))
