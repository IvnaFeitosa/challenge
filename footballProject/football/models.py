from django.db import models

# Represents a league or championship (e.g., Premier League, Bundesliga)
class League(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Represents a team in the league
class Team(models.Model):
    name = models.CharField(max_length=100)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Represents a player with details like position and team
class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    position = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Represents a match between two teams with match details
class Match(models.Model):
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches')
    date = models.DateTimeField()
    stadium = models.CharField(max_length=100)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    final_score = models.CharField(max_length=10, blank=True, null=True)  # e.g., "2-1"
    referee = models.CharField(max_length=100, blank=True, null=True)

# Statistics model for each match
class MatchStatistics(models.Model):
    match = models.OneToOneField(Match, on_delete=models.CASCADE)
    yellow_cards = models.IntegerField(default=0)
    red_cards = models.IntegerField(default=0)
    injuries = models.IntegerField(default=0)

# Individual performance for each player in a specific match
class PlayerPerformance(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    fouls_committed = models.IntegerField(default=0)
    injury = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        unique_together = ('match', 'player')
