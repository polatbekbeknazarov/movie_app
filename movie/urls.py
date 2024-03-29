from django.urls import path
from .views import movie_list, movie_detail, actor_detail, rate_movie, add_to_list

urlpatterns = [
    path('', movie_list, name='movie_list'),
    path('movie/<slug:movie_slug>/', movie_detail, name='movie_detail'),
    path('actor/<slug:actor_slug>/', actor_detail, name='actor_detail'),
    path('director/<slug:director_slug>/', actor_detail, name='director_detail'),
    path('rate_movie/<slug:movie_slug>/', rate_movie, name='rate_movie'),
    path('add_to_list/<slug:movie_slug>', add_to_list, name='add_to_list'),
]
