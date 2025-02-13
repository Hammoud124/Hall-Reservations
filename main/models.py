from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['user__first_name', 'user__last_name']


class City(models.Model):
    name = models.CharField(max_length=100)


class HallImage(models.Model):
    image = models.ImageField(upload_to='main/images')
    hall = models.ForeignKey('Hall', on_delete=models.CASCADE, related_name='images')


class Hall(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    price = models.IntegerField()


class Reservation(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    hall = models.ForeignKey('Hall', on_delete=models.CASCADE)
    reservation_date = models.DateTimeField()
    expire_date = models.DateTimeField()
