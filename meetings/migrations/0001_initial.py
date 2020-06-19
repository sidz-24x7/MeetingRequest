# Generated by Django 3.0.7 on 2020-06-18 11:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_number', models.CharField(blank=True, max_length=50, verbose_name='Contact Number')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='meetings.Department')),
                ('designation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='meetings.Designation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Meetings',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('subject', models.TextField(max_length=100, verbose_name='Purpose/Subject')),
                ('company', models.CharField(max_length=500)),
                ('designation', models.TextField(max_length=200)),
                ('name', models.CharField(max_length=100, verbose_name='Full Name')),
                ('email', models.EmailField(max_length=100, verbose_name='Official EMail')),
                ('contact_no', models.CharField(max_length=10, verbose_name='Contact Number')),
                ('date_time1', models.DateTimeField(verbose_name='Proposed Date & Time - Option 1')),
                ('duration1', models.IntegerField(verbose_name='Proposed Duration(minutes) - Option 1')),
                ('date_time2', models.DateTimeField(verbose_name='Proposed Date & Time - Option 2')),
                ('duration2', models.IntegerField(verbose_name='Proposed Duration(minutes) - Option 2')),
                ('date_time3', models.DateTimeField(verbose_name='Proposed Date & Time - Option 3')),
                ('duration3', models.IntegerField(verbose_name='Proposed Duration(minutes) - Option 3')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('requested_official', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='meetings.Employee', verbose_name='Official')),
            ],
        ),
    ]
