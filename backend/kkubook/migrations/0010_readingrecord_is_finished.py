# Generated by Django 4.2.21 on 2025-05-25 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kkubook", "0009_alter_readingrecord_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="readingrecord",
            name="is_finished",
            field=models.BooleanField(default=False),
        ),
    ]
