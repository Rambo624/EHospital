from django.db import models
from userauth import models as userauth_models

from django.utils import timezone
# Create your models here.



class Patient(models.Model):
    user=models.OneToOneField(userauth_models.User,on_delete=models.CASCADE)
    image=models.FileField(upload_to='images',null=True,blank=True)
    specialization=models.CharField(max_length=100,null=True,blank=True)
    full_name=models.CharField(max_length=100,null=True,blank=True)
    mobile=models.CharField(max_length=100,null=True,blank=True)
    blood_group=models.CharField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    gender=models.CharField(max_length=100,null=True,blank=True)
    DOB=models.DateField(default=timezone.now,null=True,blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.full_name}"


class Notification(models.Model):
    NOTIFICATION_TYPE=(
    ('appointment Scheduled','appointment Scheduled'),
    ('appointment cancelled','appointment cancelled')
)
    patient=models.ForeignKey(Patient,on_delete=models.SET_NULL,null=True,blank=True)
    appointment=models.ForeignKey('base.Appointments',on_delete=models.CASCADE,null=True,blank=True,related_name='patient_appointment_notification')
    type=models.CharField(max_length=100,choices=NOTIFICATION_TYPE)
    seen=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural="Notification"
    
    def __str__(self):
        return f"{self.patient.full_name} Notification"