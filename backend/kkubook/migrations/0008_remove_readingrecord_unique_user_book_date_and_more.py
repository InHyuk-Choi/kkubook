# Generated by Django 4.2.21 on 2025-05-25 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("kkubook", "0007_remove_readingrecord_unique_user_date_and_more"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="readingrecord",
            name="unique_user_book_date",
        ),
        migrations.AddField(
            model_name="readingrecord",
            name="last_updated",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="readingrecord",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
