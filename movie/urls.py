from django.urls import path
from .views import movie_list, movie_detail, actor_detail

urlpatterns = [
    path('', movie_list, name='movie_list'),
    path('<slug:movie_slug>/', movie_detail, name='movie_detail'),
    path('actor/<slug:actor_slug>/', actor_detail, name='actor_detail'),
    path('director/<slug:director_slug>/', actor_detail, name='director_detail'),
]
