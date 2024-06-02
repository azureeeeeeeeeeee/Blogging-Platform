from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.
class Topics(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

class News(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=100, blank=True)
    topic = models.ForeignKey(Topics, on_delete=models.SET_NULL, null=True)
    body = RichTextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to="images/")

    def __sts__(self):
        return self.title + ' | ' + str(self.user)
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nama_lengkap = models.CharField(null=True, max_length=100)
    bio = models.TextField(null=True)

    def __str__(self):
        return str(self.user)