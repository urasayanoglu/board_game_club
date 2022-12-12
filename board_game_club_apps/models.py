from django.db import models

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

    def __str__(self):
        """Return a string representation of the model."""
        return self.name


