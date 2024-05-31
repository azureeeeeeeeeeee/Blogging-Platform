from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginPage, name='login'),
    path('register', views.registerPage, name='register'),

    path('', views.home, name='home'),
    path('berita/<str:pk>', views.readNews, name='berita'),
    path('tambah-berita', views.addNews, name='tambah-berita'),
]