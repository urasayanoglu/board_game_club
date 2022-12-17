from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Game, Loan
from .forms import GameForm, LoanForm

# Create your views here.
def index(request):
    """The home page for Board Game Club."""
    return render(request, 'board_game_club_apps/index.html')

@login_required
def games(request):
    """Show all board games."""
    games = Game.objects.filter(owner = request.user).order_by('status')
    context = {'games': games}
    return render(request, 'board_game_club_apps/games.html', context)

@login_required
def game(request, game_id):
    """Show a board game with loan information."""
    game = Game.objects.get(id=game_id)
    # Making sure the game belongs to the current user:
    if game.owner != request.user:
        raise Http404
    loans = game.loan_set.order_by('-loan_date')
    context = {'game': game, 'loans':loans}
    return render(request, 'board_game_club_apps/game.html', context)

@login_required
def new_game(request):
    """Add a new game."""
    if request.method != 'POST':
        # No data submitted -> create a blank form.
        form = GameForm()
    else:
        # Post data submitted -> process the data.
        form = GameForm(data = request.POST)
        if form.is_valid():
            new_game = form.save(commit=False)
            new_game.owner = request.user
            new_game.save()
            return redirect('board_game_club_apps:games')
    # Display a blank or an invalid form:
    context = {'form': form}
    return render(request, 'board_game_club_apps/new_game.html', context)

@login_required
def loanable_games(request):
    """Show all loanable board games."""
    games = Game.objects.filter(status='a').order_by('name') #filters to show only games that are available to loan.
    context = {'games': games}
    return render(request, 'board_game_club_apps/loanable_games.html', context)

@login_required
def loanable_game(request, game_id):
    """Show a board game with loan information."""
    game = Game.objects.get(id=game_id)
    loans = game.loan_set.order_by('-loan_date')
    context = {'game': game, 'loans':loans}
    return render(request, 'board_game_club_apps/loanable_game.html', context)

@login_required
def new_loan(request):  
    """Add a new game."""
    if request.method != 'POST':
        # No data submitted -> create a blank form.
        form = LoanForm()
    else:
        # Post data submitted -> process the data.
        form = LoanForm(data = request.POST)
        if form.is_valid():
            new_loan = form.save(commit=False)
            new_loan.owner = request.user
            new_loan.status = 'o'   #? how to change status from 'a' to 'o'
            new_loan.save()
            return redirect('board_game_club_apps:loanable_games')
    # Display a blank or an invalid form:
    context = {'form': form}
    return render(request, 'board_game_club_apps/new_loan.html', context)

@login_required
def my_loans(request):
    """Show loan informations."""
    loan = Loan.objects.order_by('loan_date')
    context = {'loans':loan}
    return render(request, 'board_game_club_apps/my_loans.html', context)