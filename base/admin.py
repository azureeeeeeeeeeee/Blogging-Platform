from django.contrib import admin
from .models import News, UserProfile, Topics

# Register your models here.
admin.site.register(News)
admin.site.register(UserProfile)
admin.site.register(Topics)