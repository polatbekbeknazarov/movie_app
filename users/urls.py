from django.urls import path

from .views import register, login_user

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
]
