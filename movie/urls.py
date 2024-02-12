from django.urls import path
from .views import movie_list, movie_detail, actor_detail

urlpatterns = [
    path('', movie_list, name='movie_list'),
    path('<slug:movie_slug>/', movie_detail, name='movie_detail'),
    path('actor/<int:movie_actor>/', actor_detail, name='actor_detail'),
]
