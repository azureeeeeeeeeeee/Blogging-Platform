from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class News(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)
