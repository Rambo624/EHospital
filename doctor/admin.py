from django.contrib import admin
from doctor import models
# Register your models here.

class DoctorAdmin(admin.ModelAdmin):
    list_display = [ 'user', 'full_name', 'specialization', 'qualifications', 'years_of_experiance']

class NotificationAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'appointment', 'type', 'seen', 'date']


admin.site.register(models.Doctor, DoctorAdmin)
admin.site.register(models.Notification, NotificationAdmin)
