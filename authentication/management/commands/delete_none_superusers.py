from typing import Union

from django.core.management.base import BaseCommand

from authentication.models import User


class Command(BaseCommand):
    help = "Delete Non Superusers."

    def handle(self, *args: str, **options: Union[str, int]) -> None:
        users = User.objects.all()

        for user in users:
            if not user.is_superuser:
                user.delete()

        self.stdout.write(self.style.SUCCESS("Successfully deleted none superusers."))
