from django.shortcuts import render, get_object_or_404
from .models import Movie, Actor



def movie_list(request):

    movies = Movie.objects.all()

    context = {
        'movies': movies
    }

    return render(request, 'movie/index.html', context)


def movie_detail(request, movie_slug):
    movie = get_object_or_404(Movie, slug=movie_slug)

    context = {
        'movie': movie
    }

    return render(request, 'movie/movie_detail.html', context)


def actor_detail(request, movie_actor):
    actor = Actor.objects.get(id=movie_actor)

    context = {
        'actor': actor,
    }

    return render(request, 'movie/actor_detail.html', context)