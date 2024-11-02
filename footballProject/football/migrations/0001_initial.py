# Generated by Django 5.1.2 on 2024-11-02 18:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('stadium', models.CharField(max_length=100)),
                ('final_score', models.CharField(blank=True, max_length=10, null=True)),
                ('referee', models.CharField(blank=True, max_length=100, null=True)),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.league')),
            ],
        ),
        migrations.CreateModel(
            name='MatchStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yellow_cards', models.IntegerField(default=0)),
                ('red_cards', models.IntegerField(default=0)),
                ('injuries', models.IntegerField(default=0)),
                ('match', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='football.match')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.league')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=50)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.team')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='away_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_matches', to='football.team'),
        ),
        migrations.AddField(
            model_name='match',
            name='home_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_matches', to='football.team'),
        ),
        migrations.CreateModel(
            name='PlayerPerformance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goals', models.IntegerField(default=0)),
                ('assists', models.IntegerField(default=0)),
                ('fouls_committed', models.IntegerField(default=0)),
                ('injury', models.CharField(blank=True, max_length=100, null=True)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.player')),
            ],
            options={
                'unique_together': {('match', 'player')},
            },
        ),
    ]
