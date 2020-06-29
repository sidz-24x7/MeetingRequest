from django.contrib import admin
from .models import Meetings, Department, Designation, Employee, FormOTPCaptchaPairs


admin.site.register(Meetings)
admin.site.register(Department)
admin.site.register(Designation)
admin.site.register(Employee)
admin.site.register(FormOTPCaptchaPairs)
