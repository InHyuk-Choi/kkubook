# Generated by Django 4.2.21 on 2025-05-25 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kkubook", "0003_readingrecord"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="readingrecord",
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name="readingrecord",
            constraint=models.UniqueConstraint(
                fields=("user", "created_at"), name="unique_user_date"
            ),
        ),
    ]
