import requests
from django.conf import settings
from .models import Area, Competition, Season, Team, Coach, Player, Match, Score
from django.db import transaction

BASE_URL = "https://api.football-data.org/v4"

def get_teams():
    url = f"{BASE_URL}/competitions/BSA/teams"
    headers = {
        "X-Auth-Token": settings.FOOTBALL_DATA_API_KEY,
        "Content-Type": "application/json",
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_past_matches():
    url = f"{BASE_URL}/competitions/BSA/matches"
    headers = {
        "X-Auth-Token": settings.FOOTBALL_DATA_API_KEY,
        "Content-Type": "application/json",
    }
    params = {
        "status": "FINISHED",
        "dateFrom": "2023-01-01",
        "dateTo": "2023-12-31"
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def get_upcoming_matches():
    url = f"{BASE_URL}/competitions/BSA/matches"
    headers = {
        "X-Auth-Token": settings.FOOTBALL_DATA_API_KEY,
        "Content-Type": "application/json",
    }
    params = {
        "status": "SCHEDULED"
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def fetch_and_save_data(request=None):
    with transaction.atomic():
        # Obter e salvar dados das equipes
        teams_data = get_teams()
        for team in teams_data.get('teams', []):
            # Verificar e criar a área, se necessário
            area_id = team['area']['id']
            area, _ = Area.objects.get_or_create(
                id=area_id,
                defaults={'name': team['area']['name']}
            )

            # Criar ou atualizar a equipe com a área associada
            team_obj, created = Team.objects.update_or_create(
                id=team['id'],
                defaults={
                    'name': team['name'],
                    'short_name': team.get('shortName'),
                    'tla': team['tla'],
                    'crest': team.get('crest'),
                    'address': team.get('address'),
                    'website': team.get('website'),
                    'founded': team.get('founded'),
                    'club_colors': team.get('clubColors'),
                    'venue': team.get('venue'),
                    'area': area
                }
            )

       
        past_matches_data = get_past_matches()
        for match in past_matches_data.get('matches', []):
            
            competition, _ = Competition.objects.get_or_create(
                id=match['competition']['id'],
                defaults={'name': match['competition']['name']}
            )
            season, _ = Season.objects.get_or_create(
                id=match['season']['id'],
                defaults={
                    'start_date': match['season']['startDate'],
                    'end_date': match['season']['endDate'],
                    'current_matchday': match['season'].get('currentMatchday')
                }
            )
            area, _ = Area.objects.get_or_create(
                id=match['area']['id'],
                defaults={'name': match['area']['name']}
            )

           
            try:
                home_team = Team.objects.get(id=match['homeTeam']['id'])
            except Team.DoesNotExist:
                print(f"Home team with id {match['homeTeam']['id']} not found.")
                continue
            try:
                away_team = Team.objects.get(id=match['awayTeam']['id'])
            except Team.DoesNotExist:
                print(f"Away team with id {match['awayTeam']['id']} not found.")
                continue

            
            match_obj, created = Match.objects.update_or_create(
                id=match['id'],
                defaults={
                    'utc_date': match['utcDate'],
                    'status': match['status'],
                    'matchday': match['matchday'],
                    'stage': match.get('stage'),
                    'home_team': home_team,
                    'away_team': away_team,
                    'season': season,
                    'competition': competition,
                    'area': area
                }
            )
            
            
            if match.get('score'):
                Score.objects.update_or_create(
                    match=match_obj,
                    defaults={
                        'winner': match['score'].get('winner'),
                        'duration': match['score'].get('duration', 'REGULAR'),
                        'full_time_home': match['score'].get('fullTime', {}).get('home'),
                        'full_time_away': match['score'].get('fullTime', {}).get('away'),
                        'half_time_home': match['score'].get('halfTime', {}).get('home'),
                        'half_time_away': match['score'].get('halfTime', {}).get('away'),
                    }
                )

       
        upcoming_matches_data = get_upcoming_matches()
        for match in upcoming_matches_data.get('matches', []):
            
            competition, _ = Competition.objects.get_or_create(
                id=match['competition']['id'],
                defaults={'name': match['competition']['name']}
            )
            season, _ = Season.objects.get_or_create(
                id=match['season']['id'],
                defaults={
                    'start_date': match['season']['startDate'],
                    'end_date': match['season']['endDate'],
                    'current_matchday': match['season'].get('currentMatchday')
                }
            )
            area, _ = Area.objects.get_or_create(
                id=match['area']['id'],
                defaults={'name': match['area']['name']}
            )

            
            try:
                home_team = Team.objects.get(id=match['homeTeam']['id'])
            except Team.DoesNotExist:
                print(f"Home team with id {match['homeTeam']['id']} not found.")
                continue
            try:
                away_team = Team.objects.get(id=match['awayTeam']['id'])
            except Team.DoesNotExist:
                print(f"Away team with id {match['awayTeam']['id']} not found.")
                continue

           
            match_obj, created = Match.objects.update_or_create(
                id=match['id'],
                defaults={
                    'utc_date': match['utcDate'],
                    'status': match['status'],
                    'matchday': match['matchday'],
                    'stage': match.get('stage'),
                    'home_team': home_team,
                    'away_team': away_team,
                    'season': season,
                    'competition': competition,
                    'area': area
                }
            )
