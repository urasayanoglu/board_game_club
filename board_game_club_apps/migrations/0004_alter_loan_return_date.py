# Generated by Django 4.1.4 on 2022-12-17 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board_game_club_apps', '0003_game_owner_alter_loan_return_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='return_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
