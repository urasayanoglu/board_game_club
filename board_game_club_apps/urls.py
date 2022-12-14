"""Defines URL patterns for board_game_club_apps."""

from django.urls import path
from . import views

app_name = 'board_game_club_apps'
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    # Page that shows all the loans
    path('games', views.games, name='games'),
    # Page with loans for a single game
    path('games/<int:game_id>/', views.game, name='game'),
    # Page for adding a new game
    path('new_game/', views.new_game, name='new_game'), 
]