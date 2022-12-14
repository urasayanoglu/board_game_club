from django import forms
from .models import Game, Loan

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = [
            'name',
            'genre',
            'year_published',
            'publisher',
            'number_of_players',
            'min_age',
            'difficulty',
            'description',
        ]
        labels = {
            'name': "Name of the Board Game",
            'genre': "Game Genre",
            'year_published': "Year Published",
            'publisher': "Publisher",
            'number_of_players': "Max Number of Players",
            'min_age': "Min Age Required For the Game",
            'difficulty': "Difficulty Level",
            'description': "Board Game Description",
            }

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = [
            'game_loaned',
        ]
        labels = {
            'game_loaned': "Select the desired game to be loaned from the list below:",
        }