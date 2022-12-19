# Generated by Django 4.1.4 on 2022-12-17 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board_game_club_apps', '0005_loan_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='status',
            field=models.CharField(blank=True, choices=[('o', 'On loan'), ('a', 'Available')], default='o', max_length=1),
        ),
    ]
