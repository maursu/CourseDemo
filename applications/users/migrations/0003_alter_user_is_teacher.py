# Generated by Django 4.2.2 on 2023-07-05 08:57
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_user_groups_user_user_permissions_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_teacher",
            field=models.BooleanField(
                default=False, help_text="", verbose_name="Is teacher"
            ),
        ),
    ]
