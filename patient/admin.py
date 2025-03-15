from django.contrib import admin

# Register your models here.
from django.contrib import admin
from patient import models

class PatientAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name','mobile', 'gender', 'DOB']

class NotificationAdmin(admin.ModelAdmin):
    list_display = ['patient', 'appointment', 'type', 'seen', 'date']


admin.site.register(models.Patient, PatientAdmin)
admin.site.register(models.Notification, NotificationAdmin)