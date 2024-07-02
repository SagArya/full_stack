from django.contrib import admin
from .models import Worker, Site, Attendance, AdvancePayment, Salary

admin.site.register(Worker)
admin.site.register(Site)
admin.site.register(Attendance)
admin.site.register(AdvancePayment)
admin.site.register(Salary)
