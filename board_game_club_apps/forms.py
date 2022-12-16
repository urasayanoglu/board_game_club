from django import forms
from .models import Game, Loan

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = [
            'name',
            'genre',
            'year_published',
            'description',
            'number_of_players',
            'min_age',
            'difficulty',
        ]
        labels = {
            'name': "Name of the Board Game",
            'genre': "Game Genre",
            'year_published': "Year Published",
            'publisher': "Publisher",
            'description': "Board Game Description",
            'number_of_players': "Max Number of Players",
            'min_age': "Min Age Required For the Game",
            'difficulty': "Difficulty Level",
            }

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = [
            'game_loaned',
        ]
        labels = {
            'game_loaned': "Name of the Loaned Game",
        }