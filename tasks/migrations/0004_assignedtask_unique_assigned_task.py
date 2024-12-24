# Generated by Django 5.1.3 on 2024-12-19 17:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0003_rename_chat_id_message_chat_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="assignedtask",
            constraint=models.UniqueConstraint(
                fields=("task", "user"), name="unique_assigned_task"
            ),
        ),
    ]