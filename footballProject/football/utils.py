import requests
from django.conf import settings

BASE_URL = "https://api.football-data.org/v4"

def get_teams():
    url = f"{BASE_URL}/competitions/BSA/teams"
    headers = {
        "X-Auth-Token": settings.FOOTBALL_DATA_API_KEY,  # Use the API key directly here
        "Content-Type": "application/json",
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Levanta um erro se a resposta não for 200
    return response.json()

def get_past_matches():
    url = f"{BASE_URL}/competitions/BSA/matches"
    headers = {
        "X-Auth-Token": settings.FOOTBALL_DATA_API_KEY,  # Use the API key directly here
        "Content-Type": "application/json",
    }
    params = {
        "status": "FINISHED",  # Partidas anteriores finalizadas
        "dateFrom": "2023-01-01",  # Data inicial opcional
        "dateTo": "2023-12-31"     # Data final opcional
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def get_upcoming_matches():
    url = f"{BASE_URL}/competitions/BSA/matches"
    headers = {
        "X-Auth-Token": settings.FOOTBALL_DATA_API_KEY,  # Use the API key directly here
        "Content-Type": "application/json",
    }
    params = {
        "status": "SCHEDULED"  # Próximas partidas
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()
