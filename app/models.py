from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField

class Country(models.Model):
    name = models.CharField(max_length=60)
    countrycode = models.IntegerField()
    
    def __str__(self):
        return self.name


class Capital(models.Model):
    name = models.CharField(max_length=60)
    state = models.CharField(max_length=60)
    country = models.OneToOneField(Country, on_delete=CASCADE, primary_key= True)

    def __str__(self):
        return self.name


class state(models.Model):
    name = models.CharField(max_length=70)
    code = models.IntegerField()
    country = models.OneToOneField(Country, on_delete=CASCADE, primary_key= True)



class Album(models.Model):
    title = models.CharField(max_length=60)
    artist = models.CharField(max_length=50)
    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=50)
    album = models.ForeignKey(Album ,on_delete=models.CASCADE)
    def __str__(self):
        return self.title

    
  
class Author(models.Model):
    name = models.CharField(max_length = 100)
    desc = models.TextField(max_length = 300)
    def __str__(self):
        return self.name

  
class Book(models.Model):
    title = models.CharField(max_length = 100)
    desc = models.TextField(max_length = 300)
    authors = models.ManyToManyField(Author)
    def __str__(self):
        return self.title

