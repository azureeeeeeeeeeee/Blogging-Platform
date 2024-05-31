from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import News
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import NewsForm

# Create your views here.
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'base/login.html')


def registerPage(request):
    return render(request, 'base/register.html')



def home(request):
    news = News.objects.all()
    context = {'news': news}

    return render(request, 'base/home.html', context)


def readNews(request, pk):
    news = News.objects.get(id=pk)
    context = {'news': news}

    return render(request, 'base/berita.html', context)


@login_required(login_url='/login')
def addNews(request):
    form = NewsForm()
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.user = request.user
            news.thumbnail = request.FILES.get('thumbnail')
            news.description = request.POST.get('desc')
            news.title = request.POST.get('title')
            news.save()

            return redirect('home')
        else:
            form = NewsForm()
        
    context = {'form': form}
    return render(request, 'base/form_berita.html', context)
