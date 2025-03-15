# Generated by Django 4.2.2 on 2025-03-15 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_appointments_doctor_appointments_patient_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='status',
            field=models.CharField(choices=[('Scheduled', 'Scheduled'), ('Canceled', 'Cancelled'), ('Completed', 'Completed'), ('Pending', 'Pending')], max_length=100),
        ),
        migrations.AlterField(
            model_name='billing',
            name='status',
            field=models.CharField(choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')], max_length=100),
        ),
    ]
