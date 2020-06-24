# Generated by Django 3.0.7 on 2020-06-22 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetings',
            name='company',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='meetings',
            name='designation',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='meetings',
            name='subject',
            field=models.TextField(max_length=500, verbose_name='Purpose/Subject'),
        ),
    ]
