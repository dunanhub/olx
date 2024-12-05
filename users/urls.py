from django.urls import path
from .views import register, login_user
from .views import profile

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('profile/', profile, name='profile'),
]