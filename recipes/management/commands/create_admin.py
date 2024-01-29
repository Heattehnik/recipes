from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create a superuser with specified username and password'

    def handle(self, *args, **options):
        username = 'admin'
        password = 'admin'

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.SUCCESS(f'Superuser with username "{username}" already exists.'))
        else:
            User.objects.create_superuser(username, 'admin@example.com', password)
            self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" created successfully.'))
