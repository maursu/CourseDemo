# Generated by Django 4.2.2 on 2023-07-09 16:18
import django.core.validators
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("module_parts", "0002_alter_lesson_id_alter_task_id_alter_test_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="video",
            field=models.URLField(
                blank=True, validators=[django.core.validators.URLValidator]
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="video",
            field=models.URLField(
                blank=True, validators=[django.core.validators.URLValidator]
            ),
        ),
        migrations.AlterField(
            model_name="test",
            name="video",
            field=models.URLField(
                blank=True, validators=[django.core.validators.URLValidator]
            ),
        ),
    ]
