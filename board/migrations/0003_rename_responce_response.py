# Generated by Django 4.2.4 on 2023-09-05 13:04

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0002_alter_category_subscribers_alter_post_author_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Responce',
            new_name='Response',
        ),
    ]