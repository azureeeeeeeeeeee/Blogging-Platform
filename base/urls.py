from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginPage, name='login'),
    path('register', views.registerPage, name='register'),
    path('logout', views.logoutPage, name='logout'),
    path('profile/view/<str:pk>', views.profile, name='profile'),
    path('', views.home, name='home'),
    path('profile/edit', views.updateProfile, name='update-profile'),
    path('berita/<str:pk>', views.readNews, name='berita'),
    path('tambah-berita', views.addNews, name='tambah-berita'),
]