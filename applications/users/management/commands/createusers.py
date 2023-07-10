from random import choice

from django.core.management import BaseCommand

from applications.users.models import User


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("num_of_users")

    def handle(self, *args, **options):
        num_of_users = int(options.get("num_of_users"))
        self.stdout.write(f"creating {num_of_users} users")
        User.objects.all().delete()
        users = []
        for num in range(1, num_of_users + 1):
            user = User(
                email=f"user{num}@gmail.com",
                username=f"user{num}",
                is_teacher=choice((True, False)),
            )
            users.append(user)
        User.objects.bulk_create(users)
        self.stdout.write(f"created {num_of_users} users, first 50 have password")
