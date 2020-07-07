from django.contrib import admin
from .models import Meetings, Department, Designation, Employee, FormOTP


admin.site.register(Meetings)
admin.site.register(Department)
admin.site.register(Designation)
admin.site.register(Employee)
admin.site.register(FormOTP)
