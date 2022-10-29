from django.db import models
class User(models.Model):
    user_name = models.CharField(max_length=20)
    user_id = models.IntegerField()
    mail = models.EmailField(max_length=256)
    password = models.CharField(max_length=16)
class Flight(models.Model):
    flight_id = models.IntegerField()
    date_time = models.DateTimeField()
    destination = models.CharField(max_length=50)
class Booking(models.Model):
    user_id = models.IntegerField()
    flight_id = models.IntegerField()
    seat_number = models.IntegerField()