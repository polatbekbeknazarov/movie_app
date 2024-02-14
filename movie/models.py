from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True, default=None)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, default=None)
    image = models.ImageField(upload_to='uploads/director/', null=True, default=None)
    bio = models.TextField()
    slug=models.SlugField(null=True, default=None)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, default=None)
    image = models.ImageField(upload_to='uploads/actor', null=True, default=None)
    bio = models.TextField()
    slug=models.SlugField(null=True, default=None)

    def __str__(self):
        return self.name


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name='movie_rating')
    value = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return str(self.value)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    release_date = models.DateField()
    director = models.ForeignKey('Director', on_delete=models.CASCADE)
    actors = models.ManyToManyField('Actor')
    image = models.ImageField(upload_to='uploads/movie/', null=True, default=None)
    description = models.TextField()
    rating = models.FloatField(null=True, blank=True)
    slug = models.SlugField(null=True, default=None)

    def __str__(self):
        return self.title

    
