from django.db import models
from django.utils.timezone import now
import string
import random

# Create your models here.

def generate_unique_code():
    lenght = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=lenght)) #6 haneli random code uretiyor
        if Room.objects.filter(code=code).count() == 0:
            break

    return code

class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

  