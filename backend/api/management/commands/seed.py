import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Seed database with fake data'

    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        self.clean_data()

        self.stdout.write("Creating new data...")
        fake = Faker()

        # Create Users and Casa
        self.create_users(fake, 20)

    def clean_data(self):
        """ Remove old data from the database """
        User.objects.all().delete()

    def create_users(self, fake, count):
        for _ in range(count):
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password='password'
            )
            
        User.objects.create_superuser('admin', '', '1234')

