from django.db import models


# Create your models here.
class Driver(models.Model):
    Username = models.CharField(max_length=100)
    First_Name = models.CharField(max_length=100)
    Second_Name = models.CharField(max_length=100)
    ID_No = models.CharField(max_length=100)
    Age = models.PositiveIntegerField()
    Avatar = models.ImageField()

    def __str__(self):
        return self.Username

    class Meta:
        verbose_name_plural = 'Drivers'
