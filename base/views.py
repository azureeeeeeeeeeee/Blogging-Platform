from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import News, Topics, UserProfile
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import NewsForm
from django.contrib import messages

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
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            messages.error(request, 'Password do not match')
        else:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()

                UserProfile.objects.create(
                    user=user
                )

                login(request, user)
                messages.success(request, 'Registration successful')
                return redirect('home')
    return render(request, 'base/register.html')


def logoutPage(request):
    logout(request)
    return redirect('home')


def home(request):
    q = request.GET.get('q', '')
    news = News.objects.all()
    news = news.filter(Q(title__icontains=q) | 
                        Q(description__icontains=q))
    topics = Topics.objects.all()
    context = {'news': news, 'topics': topics}

    return render(request, 'base/home.html', context)


def readNews(request, pk):
    news = News.objects.get(id=pk)
    context = {'news': news}

    return render(request, 'base/berita.html', context)


@login_required(login_url='/login')
def addNews(request):
    form = NewsForm()
    topics = Topics.objects.all()
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)

            topic_name = request.POST.get('topic')
            topic, created = Topics.objects.get_or_create(name=topic_name)

            news.user = request.user
            news.thumbnail = request.FILES.get('thumbnail')
            news.description = request.POST.get('desc')
            news.title = request.POST.get('title')
            news.topic = topic
            
            news.save()

            return redirect('home')
        else:
            form = NewsForm()
        
    context = {'form': form, 'topics': topics}
    return render(request, 'base/form_berita.html', context)


def profile(request, pk):
    user = User.objects.get(id=pk)
    news = user.news_set.all()
    context = {'user': user, 'news':news}
    return render(request, 'base/profile.html', context)


def updateProfile(request):
    user = UserProfile.objects.get(id=request.user.id)
    print(user.nama_lengkap)
    print(user.bio)
    if request.method == 'POST':
        user.nama_lengkap = request.POST.get('full-name').title()
        user.bio = request.POST.get('user-bio')
        user.save()

        return redirect('home')

    context= {'user':user}
    return render(request, 'base/form_user.html', context)