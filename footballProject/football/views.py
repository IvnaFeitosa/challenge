from django.http import JsonResponse
from .utils import fetch_and_save_data

def teams_view(request):
    try:
        fetch_and_save_data()  
        return JsonResponse({'message': 'Dados das equipes salvos  sucesso'})
    except Exception as e:
        return JsonResponse({'error': f'Erro ao salvar dados das equipes: {str(e)}'})

def past_matches_view(request):
    try:
        fetch_and_save_data()  
        return JsonResponse({'message': 'Dados das partidas passadas salvos com sucesso'})
    except Exception as e:
        return JsonResponse({'error': f'Erro ao salvar dados das partidas passadas: {str(e)}'})

def upcoming_matches_view(request):
    try:
        fetch_and_save_data()  
        return JsonResponse({'message': 'Dados das próximas partidas salvos com sucesso'})
    except Exception as e:
        return JsonResponse({'error': f'Erro ao salvar dados das próximas partidas: {str(e)}'})
