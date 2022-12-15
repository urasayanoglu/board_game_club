from django.shortcuts import render, redirect 
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    """Register a new Board Game Club User"""
    if request.method != 'POST':
        # Display an empty form
        form = UserCreationForm()
    else:
        # Process input from data
        form = UserCreationForm(data = request.POST)
        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.
            login(request, new_user)
            return redirect('board_game_club_apps:index')
    # Display an empty or invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)
    
