from rest_framework import serializers
from .models import Estudante, Curso, Matricula
from .validators import cpf_invalido, nome_invalido, celular_invalido


class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:        
        model = Estudante
        fields = ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']

    def validate(self, data):
        if cpf_invalido(data['cpf']):
            raise serializers.ValidationError({'cpf':'CPF deve ter 11 dígitos'})
        if nome_invalido(data['nome']):
            raise serializers.ValidationError({'nome':'Nome deve conter apenas letras'})
        if celular_invalido(data['celular']):
            raise serializers.ValidationError({'celular':'Celular deve ter 13 dígitos'})
        return data
    
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
        

