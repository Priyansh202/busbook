# In your app's migrations directory, create a new Python file, e.g., '0002_create_profiles.py'

from django.db import migrations
from django.contrib.auth.models import User
from ..models import Profile


def create_profiles(apps, schema_editor):
    for user in User.objects.all():
        Profile.objects.get_or_create(user=user)


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),  # Update with your actual app name and the previous migration file
    ]

    operations = [
        migrations.RunPython(create_profiles),
    ]
