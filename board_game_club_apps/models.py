from django.db import models
from django.contrib.auth.models import User
import datetime
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

    class Return_date(models.Model):
        event_date = models.DateField()
        return_due_date = models.DateField()

        class Meta:
            ordering = ["return_due_date"]

        def save(self, *args, **kwargs):
            if self.return_due_date is None:
                 self.return_due_date = self.event_date.date() + datetime.timedelta(weeks=2)
            super(Return_date, self).save(*args, **kwargs)

    game_loaned = models.ForeignKey(Game, on_delete=models.CASCADE)
    loan_date = models.DateTimeField(auto_now_add=True)
    return_date = Return_date() # It seems that this is working now, but it's not printing in my_loans.html.
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'loans'

    def __str__(self):
        """Return a string representation of the loan model."""
        return f"Game {self.game_loaned} borrowed on {self.loan_date}"
    
    def statuschange(self):
        """Change the status of the board game to on loan"""
        return Game.status('o')

class Return(models.Model):
    """Representation of returninging a board game."""

    game_returned = models.ForeignKey(Game, on_delete=models.CASCADE)
    return_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'loans'

    def __str__(self):
        """Return a string representation of the return model."""
        return f"Game {self.game_returned} returned on {self.return_date}"
    
    def statuschange(self):
        """Change the status of the board game to on loan"""

        if Game.status == 'o':
            return Game.status('a')
        else:
            print("This game was not on loan.")

    

