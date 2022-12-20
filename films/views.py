from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import *

# Create your views here.

def main(request):
    films = Films.objects.all()
    return render(request, 'films/main.html', {'films': films})

def add(request):
    create_category()
    if request.method == 'POST':
        films = Films()
        films.name = request.POST.get('name')
        films.category_id = request.POST.get('category')
        films.date_release = request.POST.get('date_relaese')
        films.actors = request.POST.get('actors')
        films.date_show = request.POST.get('date_show')
        films.image = request.POST.get('image')
        films.save()
        return HttpResponseRedirect('/')
    categories = Category.objects.all()
    return render(request, 'films/add.html', {'categories': categories})

def create_category():
    if Category.objects.all().count() == 0:
        Category.objects.create(name = 'Ужасы')
        Category.objects.create(name = 'Боевик')
        Category.objects.create(name = 'Комедия')

def edit(request, id):
    try:
        film = Films.objects.get(id=id)

        if request.method == 'POST':
            film.name = request.POST.get('name')
            film.category_id = request.POST.get('category')
            film.date_release = request.POST.get('date_release')
            film.actors = request.POST.get('actors')
            film.date_show = request.POST.get('date_show')
            film.image = request.POST.get('image')
            film.save()
            return HttpResponseRedirect('/')
        else:
            categories = Category.objects.all()
            return render(request, 'films/edit.html', {'film':  film, 'categories':  categories})
    except Films.DoesNotExist:
        return HttpResponseNotFound('<h2>Product not found</h2>')

def delete(request, id):
    try:
        film = Films.objects.get(id=id)
        film.delete()
        return HttpResponseRedirect('/')
    except Films.DoesNotExist:
        return HttpResponseNotFound('<h2>Product not found</h2>')