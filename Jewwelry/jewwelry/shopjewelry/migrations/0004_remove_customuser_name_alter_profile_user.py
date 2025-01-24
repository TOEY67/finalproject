# Generated by Django 5.0.6 on 2025-01-08 17:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shopjewelry", "0003_customuser_image_profile"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="name",
        ),
        migrations.AlterField(
            model_name="profile",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
