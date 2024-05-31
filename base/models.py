from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.
class News(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=100, blank=True)
    body = RichTextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to="images/")

    def __sts__(self):
        return self.title or "Untitled News"