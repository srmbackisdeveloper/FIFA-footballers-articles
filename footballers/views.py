from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import *

menu = [
    {'title': "About us", 'url_name': 'about'},
    {'title': "Add page", 'url_name': 'addpage'},
    {'title': "Contact", 'url_name': 'contact'},
    {'title': "Login", 'url_name': 'login'}
    ]

def index(request):
    posts = Footballers.objects.all()
    categories = Category.objects.all()

    context = {
        'categories': categories,
        'posts': posts,
        'menu': menu,
        'title': 'Main page',
        'category_selected': ''
    }

    return render(request, 'footballers/index.html', context=context)


def about(request):
    context = {
        'menu': menu,
        'title': 'About us page'
    }

    return render(request, 'footballers/about.html', context=context)


def addpage(request):
    context = {
        'menu': menu,
        'title': 'Addpage page'
    }

    return render(request, 'footballers/addpage.html', context=context)


def contact(request):
    context = {
        'menu': menu,
        'title': 'Contact page'
    }

    return render(request, 'footballers/contact.html', context=context)


def login(request):
    context = {
        'menu': menu,
        'title': 'Login page'
    }

    return render(request, 'footballers/login.html', context=context)


def show_post(request, post_id, post_info='nothing loaded'):
    return HttpResponse(f"Post of footballer with id: {post_id}<br>{post_info}")

def show_category(request, category_name):
    posts = Footballers.objects.filter(cat__name__iexact=category_name)
    categories = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'categories': categories,
        'posts': posts,
        'menu': menu,
        'title': 'Category results',
        'category_selected': category_name
    }

    return render(request, 'footballers/index.html', context=context)

# Not found 404 response
def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>The page not found</h1><p>by: srm</p>")
