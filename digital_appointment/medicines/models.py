"""Medicines app models"""
from django.db import models
from accounts.models import User

# Create your models here.


class Location(models.Model):
    """Class representing a location"""
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Service(models.Model):
    """Class representing a Service"""
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    duration = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Provider(models.Model):
    """Class representing a Provider"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    speciality = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - as {self.speciality}"
