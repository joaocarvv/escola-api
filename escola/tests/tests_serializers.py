from django.test import TestCase
from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculaCursoSerializer

class SerializerEstudanteTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante(
            nome = 'Teste de Serializer',
            email = 'testedeserializer@gmail.com',
            cpf = '01119001072',
            data_nascimento = '2023-01-01',
            celular = '86 99999-9999',
        )
        self.serializer = EstudanteSerializer(instance=self.estudante)

    def test_verifica_campos_serializer_de_estudante(self):
        """Teste que verifica os campos do serializer de Estudante"""

        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']))

    def test_verifica_campos_serializer_de_estudante(self):
        """Teste que verifica o conteudo dos campos do serializer de Estudante"""
        # data = dados
        data = self.serializer.data
        self.assertEqual(data['nome'], self.estudante.nome)
        self.assertEqual(data['email'], self.estudante.email)
        self.assertEqual(data['cpf'], self.estudante.cpf)
        self.assertEqual(data['data_nascimento'], self.estudante.data_nascimento)
        self.assertEqual(data['celular'], self.estudante.celular)

class SerializerCursoTestCase(TestCase):
    def setUp(self):   
        self.curso = Curso(
            codigo = 'POO',
            descricao = 'Programação Orientada a Objetos',
            nivel = 'B',
        )
        self.serializer = CursoSerializer(instance=self.curso)

    def test_verifica_campos_serializer_de_curso(self):
        """Teste que verifica os campos do serializer de Curso"""

        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'codigo', 'descricao', 'nivel']))

    def test_verifica_campos_serializer_de_curso(self):
        """Teste que verifica o conteudo dos campos do serializer de Curso"""
        data= self.serializer.data
        self.assertEqual(data['codigo'], self.curso.codigo)
        self.assertEqual(data['descricao'], self.curso.descricao)
        self.assertEqual(data['nivel'], self.curso.nivel)
                         
class SerializerMatriculaTestCase(TestCase):
    def setUp(self):
        self.estudante_matricula = Estudante.objects.create(
            nome = 'Teste de Serializer',
            email = 'testedeserializer@gmail.com',
            cpf = '01119001072',
            data_nascimento = '2023-01-01',
            celular = '86 99999-9999',
        )
        self.curso_matricula = Curso.objects.create(
            codigo='POO',
            descricao='Programação Orientada a Objetos',
            nivel='B',
        )
        self.matricula = Matricula.objects.create(
            estudante=self.estudante_matricula,
            curso=self.curso_matricula,
            periodo='M',
        )
        self.serializer = MatriculaSerializer(instance=self.matricula)

    def test_verifica_campos_serializer_de_matricula(self):
        """Teste que verifica os campos do serializer de Matricula"""

        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'estudante', 'curso', 'periodo']))

    def test_verifica_campos_serializer_de_matricula(self):
        data = self.serializer.data
        self.assertEqual(data['estudante'], self.estudante_matricula.id)
        self.assertEqual(data['curso'], self.curso_matricula.id)
        self.assertEqual(data['periodo'], self.matricula.periodo)        