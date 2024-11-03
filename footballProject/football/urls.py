from django.urls import path
from . import views

urlpatterns = [
    path('teams/', views.teams_view, name='teams'),
    path('matches/', views.past_matches_view, name='past_matches'),
    path('upcoming-matches/', views.upcoming_matches_view, name='upcoming_matches'),
]
