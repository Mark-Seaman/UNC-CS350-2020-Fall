from django.core.management.base import BaseCommand

from plan.coder import build_code


class Command(BaseCommand):

    def handle(self, *args, **options):
        build_code()
