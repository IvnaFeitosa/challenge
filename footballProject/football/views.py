# views.py
import requests
from django.http import JsonResponse
from django.views import View
from .models import models


class FetchDataFromAPI(View):
    def get(self, request):
        
        url = 'https://api.football-data.org/v4/competitions/?areas=2032'
        headers = {
            'X-Auth-Token': '566461e47e184fa88db7f9d0d7a1dbac',  
        }

        # Fazendo a requisição à API
        response = requests.get(url, headers=headers)

        # Verifica se a requisição foi bem-sucedida
        if response.status_code == 200:
            data = response.json()  # Converte a resposta para JSON
            return JsonResponse(data)  # Retorna a resposta como JSON
        else:
            return JsonResponse({'error': 'Erro ao acessar a API'}, status=response.status_code)