from django.shortcuts import render, redirect
from .models import Game
from .forms import GameForm

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

def new_game(request):
    """Add a new game."""
    if request.method != 'POST':
        # No data submitted -> create a blank form.
        form = GameForm()
    else:
        # Post data submitted -> process the data.
        form = GameForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_game_club_apps:games')
    # Display a blank or an invalid form:
    context = {'form': form}
    return render(request, 'board_game_club_apps/new_game.html', context)