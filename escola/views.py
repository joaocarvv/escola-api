from .models import Estudante, Curso
from .serializers import EstudanteSerializer, CursoSerializer
from rest_framework import viewsets


class EstudanteViewSet(viewsets.ModelViewSet):
    """Exibindo todos os estudantes"""
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer




