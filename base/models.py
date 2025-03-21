from django.db import models
from doctor import models as doctor_models
from patient import models as patient_models
from shortuuid.django_fields import ShortUUIDField
# Create your models here.




class Service(models.Model):
    image=models.FileField(upload_to='images',null=True,blank=True)
    name=models.CharField(max_length=100,null=True,blank=True)
    description=models.CharField(max_length=500,null=True,blank=True)
    cost=models.DecimalField(max_digits=10,decimal_places=2)
    available_doctors=models.ManyToManyField(doctor_models.Doctor,blank=True)

    def __str__(self):
        return self.name


class Appointments(models.Model):
    STATUS=[
    ("Scheduled","Scheduled"),
    ("Canceled","Cancelled"),
    ("Completed","Completed"),
    ("Pending","Pending")
]
    service=models.ForeignKey(Service,on_delete=models.CASCADE,null=True,blank=True,related_name="service_appointments")
    patient=models.ForeignKey(patient_models.Patient,on_delete=models.CASCADE,null=True,blank=True,related_name='patient_appointment')
    doctor=models.ForeignKey(doctor_models.Doctor,on_delete=models.CASCADE,null=True,blank=True,related_name='doctor_appointment')
    appointment_date=models.DateTimeField(null=True,blank=True)
    issues=models.TextField(null=True,blank=True)
    symptoms=models.TextField(null=True,blank=True)
    appointment_id=ShortUUIDField(length=6,max_length=10,alphabet="1234567890")
    status=models.CharField(max_length=100,choices=STATUS)

    def __str__(self):
        return f"{self.patient.full_name} with Dr.{self.doctor.full_name}"
    
class MedicalRecord(models.Model):
    appointment=models.ForeignKey(Appointments,on_delete=models.CASCADE)
    treatment=models.TextField()
    diagnosis=models.TextField()

    def __str__(self):
        return f"Medical record of {self.appointment.patient.full_name}"

class Labtest(models.Model):
    appointment=models.ForeignKey(Appointments,on_delete=models.CASCADE)
    test_name=models.CharField(max_length=200)
    description=models.TextField(blank=True,null=True)
    result=models.TextField(blank=True,null=True)

class Prescription(models.Model):
    appointment=models.ForeignKey(Appointments,on_delete=models.CASCADE)
    medications=models.TextField(blank=True,null=True)

    def __str__(self):
        return f"Prescriptions for {self.appointment.patient.full_name}"

class Billing(models.Model):
    patient=models.ForeignKey(patient_models.Patient,on_delete=models.SET_NULL,null=True,blank=True,related_name='patient_billing')
    appointment=models.ForeignKey(Appointments,on_delete=models.CASCADE,null=True,blank=True,related_name='billing')
    sub_total=models.DecimalField(max_digits=10,decimal_places=2)
    tax=models.DecimalField(max_digits=10,decimal_places=2)
    total=models.DecimalField(max_digits=10,decimal_places=2)
    status=models.CharField(max_length=100,choices=[('Paid','Paid'),('Unpaid','Unpaid')])
    billing_id=ShortUUIDField(length=6,max_length=10,alphabet='1234567890')
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Billing for {self.patient.full_name}-Total={self.sub_total}"