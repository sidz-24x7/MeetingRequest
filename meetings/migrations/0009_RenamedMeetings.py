# Generated by Django 3.0.7 on 2020-07-10 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0008_UpdatedTableName'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Meetings',
            new_name='Meeting',
        ),
    ]
