"""Defines URL patterns for board_game_club_apps."""

from django.urls import path
from . import views

app_name = 'board_game_club_apps'
urlpatterns = [
    # Home Page
    path('', views.index, name='index'), 
]