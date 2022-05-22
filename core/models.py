from django.db import models

Fuel_Choices = [
    ('petrol', 'petrol'),
    ('diesel', 'diesel'),
]

Transmission_Choices = [
    ('Auto', 'Auto'),
    ('Manual', 'Manual'),
]


# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField()
    description = models.CharField(max_length=300)
    capacity = models.PositiveIntegerField()
    plate_no = models.CharField(max_length=100)
    fuel = models.CharField(max_length=100, choices=Fuel_Choices)
    Transmission = models.CharField(max_length=100, choices=Transmission_Choices)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cars'


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Contacts'


