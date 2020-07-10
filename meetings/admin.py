from django.contrib import admin
from .models import Meeting, Department, Designation, Employee, FormOTP


admin.site.register(Meeting)
admin.site.register(Department)
admin.site.register(Designation)
admin.site.register(Employee)
admin.site.register(FormOTP)
