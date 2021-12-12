from django.shortcuts import render
from .models import *

# Create your views here.
def onetoone(request):
    country = Country.objects.all()
    capital = Capital.objects.all()
    sta = state.objects.all()
    return render(request,"home.html",{"country":country,"capital":capital,"sta":sta})
      
def manytoone(request):
    album = Album.objects.all()
    song = Song.objects.all()
    return render(request,"onetomany.html",{"album":album,"song":song})

def manytomany(request):
    auther = Author.objects.all()
    book = Book.objects.all()
    return render(request,"manytomany.html",{"auther":auther,"book":book})