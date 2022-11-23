from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *


@login_required(login_url='/users/sign_in')
def home(request):
    news = News.objects.all().order_by('date_added')
    return render(request, 'home.html', {'news': news})


def detail(request, slug):
    news = News.objects.get(slug=slug)
    news.views += 1
    news.save()
    return render(request, 'detail.html', {'news': news})


def like(request, slug):
    news = News.objects.get(slug=slug)

    if request.user not in news.likes.all():
        news.likes.add(request.user)
    elif request.user in news.likes.all():
        news.likes.remove(request.user)
    return redirect('newspage:detail', slug=news.slug)
