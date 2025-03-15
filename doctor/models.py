from django.db import models
from userauth import models as userauth_models

from django.utils import timezone
# Create your models here.


class Doctor(models.Model):
    user=models.OneToOneField(userauth_models.User,on_delete=models.CASCADE)
    image=models.FileField(upload_to='images',null=True,blank=True,default='images/default.jpg')
    specialization=models.CharField(max_length=100,null=True,blank=True)
    full_name=models.CharField(max_length=100,null=True,blank=True)
    mobile=models.CharField(max_length=100,null=True,blank=True)
    bio=models.CharField(max_length=100,null=True,blank=True)
    years_of_experiance=models.CharField(max_length=100,null=True,blank=True)
    qualifications=models.CharField(max_length=100,null=True,blank=True)
    next_available_appointment_date=models.DateTimeField(default=timezone.now,null=True,blank=True)

    def __str__(self):
        return f"Dr.{self.full_name}"


class Notification(models.Model):
    NOTIFICATION_TYPE=(
    ('New appointment','New appointment'),
    ('appointment cancelled','appointment cancelled')
)

    doctor=models.ForeignKey(Doctor,on_delete=models.SET_NULL,null=True,blank=True)
    appointment=models.ForeignKey('base.Appointments',on_delete=models.CASCADE,null=True,blank=True,related_name='doctor_appointment_notification')
    type=models.CharField(max_length=100,choices=NOTIFICATION_TYPE)
    seen=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural="Notification"
    
    def __str__(self):
        return f"Dr.{self.doctor.full_name} Notification"