# Generated by Django 4.2.2 on 2025-03-15 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_alter_doctor_next_available_appointment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.FileField(blank=True, default='images/default.jpg', null=True, upload_to='images'),
        ),
    ]
