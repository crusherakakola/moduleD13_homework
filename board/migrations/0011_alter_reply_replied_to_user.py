# Generated by Django 4.2.4 on 2023-09-15 09:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0010_alter_reply_replied_to_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='replied_to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to=settings.AUTH_USER_MODEL),
        ),
    ]
