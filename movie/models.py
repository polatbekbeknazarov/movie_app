from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


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
    title = models.CharField(max_length=255, verbose_name='Название')
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, verbose_name='Жанр')
    release_date = models.DateField(verbose_name='Дата релиза')
    director = models.ForeignKey('Director', on_delete=models.CASCADE, verbose_name='Режиссер')
    actors = models.ManyToManyField('Actor', verbose_name='Актеры')
    image = models.ImageField(upload_to='uploads/movie/', null=True, default=None, verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание')
    video = models.FileField(upload_to='uploads/video', 
                             null=True, default=None, 
                             validators=[FileExtensionValidator(allowed_extensions=['mp4'])],
                             verbose_name='Видео'
                             )
    rating = models.FloatField(null=True, blank=True, verbose_name='Оценки')
    slug = models.SlugField(null=True, default=None)

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.title


class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


class MovieComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
