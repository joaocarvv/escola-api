from rest_framework import serializers
from .models import Estudante, Curso, Matricula

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:        
        model = Estudante
        fields = ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []

class ListaMatriculaEstudanteSerializer(serializers.ModelSerializer):
    #Apenas visualizar e mostrar a descrição do curso
    curso= serializers.ReadOnlyField(source='curso.descricao')
    periodo= serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso','periodo']
    #Verificar se é M, V ou N e pegar o valor que foi definido ex: vai retornar Matutino se for M
    def get_periodo(self, obj):
        return obj.get_periodo_display()

class ListaMatriculaCursoSerializer(serializers.ModelSerializer):
    #Apenas visualizar e mostrar o nome do estudante
    estudante_nome = serializers.ReadOnlyField(source='estudante.nome')
    class Meta:
        model = Matricula
        fields = ['estudante_nome']
        

