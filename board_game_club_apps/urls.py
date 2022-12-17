"""Defines URL patterns for board_game_club_apps."""

from django.urls import path
from . import views

app_name = 'board_game_club_apps'
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    # Page that shows all the games
    path('games', views.games, name='games'),
    # Page that shows all loanable games
    path('loanable_games/', views.loanable_games, name='loanable_games'),
    # Page with loans for a single game
    path('games/<int:game_id>/', views.game, name='game'),
    # Page with loans for a loanable game
    path('loanable_games/<int:game_id>/', views.loanable_game, name='loanable_game'),
    # Page for adding a new game
    path('new_game/', views.new_game, name='new_game'), 
    # Page for loaning a new game
    path('new_loan/', views.new_loan, name='new_loan'),
    # Page that shows current loans of a user
    path('my_loans', views.my_loans, name='my_loans'),
]