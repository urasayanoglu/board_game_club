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
    # Page with about info of a single game
    path('games/<int:game_id>/', views.game, name='game'),
    # Page for editing a board game
    path('edit_game/<int:game_id>/', views.edit_game, name="edit_game"),
    # Page with about info of a loanable game
    path('loanable_games/<int:game_id>/', views.loanable_game, name='loanable_game'),
    # Page for adding a new game
    path('new_game/', views.new_game, name='new_game'), 
    # Page for loaning a new game
    path('new_loan/', views.new_loan, name='new_loan'),
    # Page that shows current loans of a user
    path('my_loans', views.my_loans, name='my_loans'),
    #page that allows to return a game
    path('new_return', views.new_return, name = 'return_a_game'),
    # Page that shows all returnable games
    path('returnable_games/', views.returnable_games, name='returnable_games'),
    # Page with about info of a returnable game
    path('returnable_games/<int:game_id>/', views.returnable_game, name='returnable_game'),
    # Page that shows possible returns of a user
    path('my_return', views.my_return, name='my_return'),


]