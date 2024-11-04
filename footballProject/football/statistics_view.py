# views.py
from django.http import JsonResponse
from django.db.models import Q, Count
from .models import Team, Match, Score

def team_statistics_view(request):
    teams_data = []

    for team in Team.objects.all():
        # Contabilizar vitórias
        wins = Score.objects.filter(
            Q(match__home_team=team, winner='HOME_TEAM') |
            Q(match__away_team=team, winner='AWAY_TEAM')
        ).count()

        # Contabilizar derrotas
        losses = Score.objects.filter(
            Q(match__home_team=team, winner='AWAY_TEAM') |
            Q(match__away_team=team, winner='HOME_TEAM')
        ).count()

        # Contabilizar empates
        draws = Score.objects.filter(
            Q(match__home_team=team) |
            Q(match__away_team=team),
            winner='DRAW'
        ).count()

        # Dados de resposta para cada time
        team_data = {
            "id": team.id,
            "nome": team.name,
            "sigla": team.short_name,
            "escudo": team.crest,
            "vitorias": wins,
            "empates": draws,
            "derrotas": losses
        }
        
        teams_data.append(team_data)

    return JsonResponse(teams_data, safe=False)
