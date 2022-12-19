from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Game(models.Model):
    """Representation of a board game."""

    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    year_published = models.IntegerField()
    publisher = models.CharField(max_length=200)
    description = models.CharField(max_length=600)
    number_of_players = models.IntegerField()
    min_age = models.IntegerField()
    difficulty = models.CharField(max_length=100)    
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    loan_status = (
        ('o', 'On loan'),
        ('a', 'Available'),
        )
    status = models.CharField(max_length=1, choices=loan_status, blank=True, default='a')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name


class Loan(models.Model):
    """Representation of loaning a board game."""

    game_loaned = models.ForeignKey(Game, on_delete=models.CASCADE)
    loan_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True) # ? Is there a way to limit the return date for 2 weeks etc.
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'loans'

    def __str__(self):
        """Return a string representation of the loan model."""
        return f"Game {self.game_loaned} borrowed on {self.loan_date}"
    
    def statuschange(self):
        """Change the status of the board game to on loan"""
        return Game.status('o')

    

