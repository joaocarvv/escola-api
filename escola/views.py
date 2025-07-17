from .models import Estudante, Curso, Matricula
from .serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer
from rest_framework import viewsets


class EstudanteViewSet(viewsets.ModelViewSet):
    """Exibindo todos os estudantes"""
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer




