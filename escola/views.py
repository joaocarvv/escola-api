from django.http import JsonResponse

def estudantes(request):
    if request.method == 'GET':
        estudantes = {
            'id': '1',
            'nome': 'joao'
        }
        return JsonResponse(estudantes)
    

