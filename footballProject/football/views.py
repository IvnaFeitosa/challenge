# football/views.py
from django.http import JsonResponse
from .utils import get_teams, get_past_matches, get_upcoming_matches

def teams_view(request):
    teams = get_teams()
    return JsonResponse(teams)  # Respond with JSON

def past_matches_view(request):
    matches = get_past_matches()
    return JsonResponse(matches)  # Respond with JSON

def upcoming_matches_view(request):
    matches = get_upcoming_matches()
    return JsonResponse(matches)  # Respond with JSON
