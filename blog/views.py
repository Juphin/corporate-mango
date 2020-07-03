from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Article


def index(request):
    data = Article.objects.all()
    return render(request, 'blog/home.html', {'articles': data})


def detail(request, id, slug):
    data = Article.objects.filter(pk=id)
    return render(request, 'blog/detail.html', {'articles': data})


def about(request):
    return render(request, 'blog/about.html', locals())

