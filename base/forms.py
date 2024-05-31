from django.forms import ModelForm
from .models import News
from django.contrib.auth.models import User


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['body']