from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Meetings(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    subject = models.TextField(verbose_name="Purpose/Subject", max_length=100)
    company = models.CharField(max_length=500)
    designation = models.TextField()
    name = models.CharField(max_length=100, verbose_name="Full Name")
    email = models.EmailField(max_length=100, verbose_name="Official EMail")
    contact_no = models.CharField(max_length=10, verbose_name="Contact Number")
    date_time = models.DateTimeField(verbose_name="Proposed Date & Time")
    created_at = models.DateTimeField(auto_now_add=True)
    requested_official = models.ForeignKey(
        'Employee', on_delete=models.SET_NULL, verbose_name="Official", null=True)

    def __str__(self):
        return self.id


class Department(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name


def get_dgh_id():
    return Department.objects.get(name="DGH").pk


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(
        'Department', on_delete=models.SET_DEFAULT, default=get_dgh_id)
    designation = models.CharField(max_length=200, blank=True)
    contact_number = models.CharField(
        max_length=50, blank=True, verbose_name="Contact Number")

    def __str__(self):
        return self.user.first_name + "  " + self.user.last_name
