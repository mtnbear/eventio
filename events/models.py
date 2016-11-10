from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    owner = models.ForeignKey(User, related_name='authored_events')
    price = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=6)
    capacity = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
