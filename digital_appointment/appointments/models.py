"""Appointment app models"""
from django.db import models
from accounts.models import User
from medicines.models import Provider, Service
# Create your models here.


class Appointment(models.Model):
    """Class representing an Appointment"""

    APPOINMENT_STATUS_CHOICES = [
        ("scheduled", "Scheduled"),
        ("canceled", "Canceled"),
        ("completed", "Completed"),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="appointments")
    provider = models.ForeignKey(
        Provider, on_delete=models.CASCADE, related_name="appointments")
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name="appointments")
    appointment_date = models.DateTimeField()
    status = models.CharField(
        max_length=20, choices=APPOINMENT_STATUS_CHOICES, default="scheduled")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} with appoinment id: {self.id}"
