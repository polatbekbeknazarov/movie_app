from django.shortcuts import render, get_object_or_404,redirect
from .models import Movie, Actor, Director, Genre, Rating
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Avg



def movie_list(request, genre_slug=None):
    genres = Genre.objects.all()

    if request.GET.get('genre'):
        genre_slug = request.GET.get('genre')
        
        genre = Genre.objects.get(slug=genre_slug)
        movies = Movie.objects.filter(genre=genre)
    else:
        movies = Movie.objects.all()

    context = {
        'movies': movies,
        'genres': genres,
    }

    return render(request, 'movie/index.html', context)


def movie_detail(request, movie_slug):
    movie = get_object_or_404(Movie, slug=movie_slug)

    context = {
        'movie': movie
    }

    return render(request, 'movie/movie_detail.html', context)


def actor_detail(request, actor_slug=None, director_slug=None):
    if actor_slug:
        staff = get_object_or_404(Actor, slug=actor_slug)
    elif director_slug:
        staff = get_object_or_404(Director, slug=director_slug)

    context = {
        'staff': staff,
    }

    return render(request, 'movie/staff_detail.html', context)

@login_required
def rate_movie(request, movie_slug):
    if request.method == 'POST':
        movie = get_object_or_404(Movie, slug=movie_slug)
        rating_value = int(request.POST.get('rating'))
        rating, created = Rating.objects.get_or_create(
            user=request.user, movie=movie, defaults={'value': rating_value}
        )

        if not created:
            rating.value = rating_value
            rating.save()

        movie.rating = Rating.objects.filter(
            movie=movie).aggregate(Avg('value'))['value__avg']
        movie.save()

        messages.success(
            request, f'Постановлена оценка {rating_value} на фильм {movie}'
        )

        return redirect('movie_detail', movie_slug=movie_slug)
    
    return redirect('movie_list')