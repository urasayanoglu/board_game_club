from django.shortcuts import render

# Create your views here.
def index(request):
    """The home page for Board Game Club."""
    return render(request, 'board_game_club_apps/index.html')