from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('games/', views.games, name='games'),
    path('signup/', views.signup, name='signup'),
    path('routine/', views.routine, name='routine'),
    path('login/', views.login, name='login'),
]
