from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class AddRoom(models.Model):
    room_no = models.CharField(max_length=10, primary_key=True, unique=True)
    room_size = models.CharField(max_length=50, blank=True, null=True)
    room_facilities = models.CharField(max_length=150, null=True, blank=True)
    room_price = models.IntegerField(blank=True, null=True)
    capacity = models.CharField(max_length=20)
    room_photo = models.ImageField(upload_to='profile/', null=True, blank=True)

    def __str__(self):
        return str(self.room_no) + str(' ') + str('No. Room')


class FillCostumerForm(models.Model):
    room_num = models.CharField(max_length=15, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    permanent_address = models.CharField(max_length=100, null=True, blank=True)
    temporary_address = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    no_of_costumer = models.CharField(max_length=50, null=True, blank=True)
    relationship = models.CharField(max_length=100, null=True, blank=True)
    contact_no = models.CharField(max_length=50, null=True, blank=True, unique=True)
    email = models.CharField(max_length=30)

    def __str__(self):
        return str(self.name) + ',' + str(self.contact_no) + ' , ' + str(self.email)


class CheckAvailable(models.Model):
    check_in_date = models.DateTimeField(null=True, blank=True)
    check_out_date = models.DateTimeField(null=True, blank=True)
    room_number = models.CharField(max_length=10)

    def __str__(self):
        return self.check_in_date
