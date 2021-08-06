from django.db import models

class Main(models.Model):
    login = models.CharField()
    password = models.CharField()
    name = models.CharField()
    nik = models.CharField()
    photo = models.ImageField(upload_to="photos/avatars")
    time_create = models.DateTimeField