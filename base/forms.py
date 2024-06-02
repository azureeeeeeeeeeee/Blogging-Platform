from django.forms import ModelForm
from .models import News
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['body']


class UpdateUserForm(UserChangeForm):
    pass