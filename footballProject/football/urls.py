from django.urls import path
from . import views
from .statistics_view import team_statistics_view 

urlpatterns = [
    path('teams/', views.teams_view, name='teams'),
    path('matches/', views.past_matches_view, name='past_matches'),
    path('upcoming-matches/', views.upcoming_matches_view, name='upcoming_matches'),
    path('statistics/', team_statistics_view, name='team_statistics'),
]
