# Generated by Django 3.0.7 on 2020-06-22 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0002_updated_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetings',
            name='designation',
            field=models.CharField(max_length=100),
        ),
    ]
