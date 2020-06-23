from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Room(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    room_name = models.CharField(max_length=10)
    room_id = models.CharField(max_length=15)

    def __str__(self):
        return self.room_id



