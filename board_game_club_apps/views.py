from django.shortcuts import render
from .models import Loan
# Create your views here.
def index(request):
    """The home page for Board Game Club."""
    return render(request, 'board_game_club_apps/index.html')

def loans(request):
    """Show all board game loans."""
    loans = Loan.objects.order_by('loan_date')
    context = {'loans': loans}
    return render(request, 'board_game_club_apps/loans.html', context)