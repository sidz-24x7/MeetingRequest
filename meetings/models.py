from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Meetings(models.Model):
    STATUS = (
        (1, 'SUBMITTED'),
        (2, 'PENDING APPROVAL'),
        (3, 'APPROVED'),
        (4, 'REJECTED'),
        (5, 'EXPIRED')
    )
    id = models.CharField(primary_key=True, max_length=100)
    subject = models.TextField(verbose_name="Purpose/Subject", max_length=500)
    company = models.CharField(max_length=200)
    designation = models.CharField(max_length=100)
    name = models.CharField(max_length=100, verbose_name="Full Name")
    email = models.EmailField(max_length=100, verbose_name="Official EMail")
    contact_no = models.CharField(max_length=10, verbose_name="Contact Number")
    date_time1 = models.DateTimeField(verbose_name="Proposed Date & Time - Option 1")
    duration1 = models.IntegerField(verbose_name="Proposed Duration(minutes) - Option 1")
    date_time2 = models.DateTimeField(verbose_name="Proposed Date & Time - Option 2", blank=True, null=True)
    duration2 = models.IntegerField(verbose_name="Proposed Duration(minutes) - Option 2", blank=True, null=True)
    date_time3 = models.DateTimeField(verbose_name="Proposed Date & Time - Option 3", blank=True, null=True)
    duration3 = models.IntegerField(verbose_name="Proposed Duration(minutes) - Option 3", blank=True, null=True)
    requested_official = models.ForeignKey('Employee', on_delete=models.SET_NULL, verbose_name="Official", null=True)
    status = models.IntegerField(verbose_name="Status", choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id + "---" + self.requested_official.designation.name


class Department(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Designation(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


def get_default_id(model_name):
    if model_name == "Department":
        return Department.objects.get(name="DGH").pk
    elif model_name == "Designation":
        return Designation.objects.get(name="DGH Employee").pk


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # department = models.ForeignKey('Department', on_delete=models.SET_DEFAULT, default=get_default_id("Department"))
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)
    # designation = models.ForeignKey('Designation', on_delete=models.SET_DEFAULT, default=get_default_id("Designation"))
    designation = models.ForeignKey('Designation', on_delete=models.SET_NULL, null=True)
    contact_number = models.CharField(max_length=50, blank=True, verbose_name="Contact Number")
    order_number = models.IntegerField(verbose_name="Site Order", unique=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name + "  " + self.user.last_name + ", " + self.designation.name


class FormOTP(models.Model):
    company = models.CharField(max_length=200)
    designation = models.CharField(max_length=100)
    name = models.CharField(max_length=100, verbose_name="Full Name")
    email = models.EmailField(max_length=100, verbose_name="Official EMail")
    contact_no = models.CharField(max_length=10, verbose_name="Contact Number")
    otp = models.IntegerField(verbose_name="Generated OTP")
    created_at = models.DateTimeField(auto_now_add=True)
    valid_till = models.DateTimeField(verbose_name="Valid Until")
