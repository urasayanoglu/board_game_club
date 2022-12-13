# Generated by Django 4.1.4 on 2022-12-13 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board_game_club_apps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='status',
            field=models.CharField(blank=True, choices=[('o', 'On loan'), ('a', 'Available')], default='a', max_length=1),
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_date', models.DateTimeField(auto_now_add=True)),
                ('return_date', models.DateTimeField(auto_now_add=True)),
                ('game_loaned', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board_game_club_apps.game')),
            ],
            options={
                'verbose_name_plural': 'loans',
            },
        ),
    ]