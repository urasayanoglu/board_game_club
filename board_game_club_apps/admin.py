from django.contrib import admin
from .models import Game, Loan, Return

# Register your models here.

admin.site.register(Game)
admin.site.register(Loan)
admin.site.register(Return)