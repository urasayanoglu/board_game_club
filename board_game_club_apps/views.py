from django.shortcuts import render
from .models import Game
# Create your views here.
def index(request):
    """The home page for Board Game Club."""
    return render(request, 'board_game_club_apps/index.html')

def games(request):
    """Show all board games."""
    games = Game.objects.order_by('status')
    context = {'games': games}
    return render(request, 'board_game_club_apps/games.html', context)

def game(request, game_id):
    """Show a board game with loan information."""
    game = Game.objects.get(id=game_id)
    loans = game.loan_set.order_by('-loan_date')
    context = {'game': game, 'loans':loans}
    return render(request, 'board_game_club_apps/game.html', context)
