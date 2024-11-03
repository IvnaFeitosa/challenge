from django.db import models


class Area(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3, null=True)
    flag = models.URLField(null=True)


class Competition(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    type = models.CharField(max_length=20)
    emblem = models.URLField(null=True)


class Season(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    current_matchday = models.PositiveIntegerField()
    winner = models.CharField(max_length=100, null=True)


class Team(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=50, null=True)
    tla = models.CharField(max_length=3)
    crest = models.URLField(null=True)
    address = models.TextField(null=True)
    website = models.URLField(null=True)
    founded = models.PositiveIntegerField(null=True)
    club_colors = models.CharField(max_length=50, null=True)
    venue = models.CharField(max_length=100, null=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    running_competitions = models.ManyToManyField(Competition)


class Coach(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    contract_start = models.DateField(null=True)
    contract_until = models.DateField(null=True)


class Player(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=50)
    team = models.ForeignKey(Team, related_name='squad', on_delete=models.CASCADE)


class Match(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    utc_date = models.DateTimeField()
    status = models.CharField(max_length=10)
    matchday = models.PositiveIntegerField()
    stage = models.CharField(max_length=20, null=True)
    home_team = models.ForeignKey(Team, related_name='home_matches', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name='away_matches', on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)


class Score(models.Model):
    match = models.OneToOneField(Match, on_delete=models.CASCADE)
    winner = models.CharField(max_length=20, null=True)
    duration = models.CharField(max_length=20, default='REGULAR')
    full_time_home = models.PositiveIntegerField(null=True)
    full_time_away = models.PositiveIntegerField(null=True)
    half_time_home = models.PositiveIntegerField(null=True)
    half_time_away = models.PositiveIntegerField(null=True)
