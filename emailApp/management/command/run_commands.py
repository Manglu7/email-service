from django.core.management.base import BaseCommand

from emailApp.consumer import handle_send_email


class Command(BaseCommand):
    def handle(self, *args, **options):
        handle_send_email()
