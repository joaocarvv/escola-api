from django.test import TestCase
from escola.models import Estudante, Curso, Matricula


class ModelEstudanteTestCase(TestCase):
    #    def teste_falha(self):
    #    self.fail('Teste falhou :(')
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = 'Teste de Modelo',
            email = 'testedemodelo@gmail.com',
            cpf = '01119001072',
            data_nascimento = '2023-01-01',
            celular = '86 99999-9999',
        )
    
    def test_verifica_atributos_de_estudante(self):
        """Teste que verifica os atributos do modelo de Estudante"""

        self.assertEqual(self.estudante.nome, 'Teste de Modelo')
        self.assertEqual(self.estudante.email, 'testedemodelo@gmail.com')
        self.assertEqual(self.estudante.cpf, '01119001072')
        self.assertEqual(self.estudante.data_nascimento, '2023-01-01')
        self.assertEqual(self.estudante.celular, '86 99999-9999')

class ModelCursoTestCase(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(
            codigo = 'POO',
            descricao = 'Programação Orientada a Objetos',
            nivel = 'B',
        )
        
    def test_verifica_atributos_de_curso(self):
        """Teste que verifica os atributos do modelo de Curso"""

        self.assertEqual(self.curso.codigo, 'POO')
        self.assertEqual(self.curso.descricao, 'Programação Orientada a Objetos')
        self.assertEqual(self.curso.nivel, 'B')


class ModelMatriculaTestCase(TestCase):
    def setUp(self):
        self.estudante_matricula = Estudante.objects.create(
            nome = 'Teste de Modelo',
            email = 'testedemodelo@gmail.com',
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

    def test_verifica_atributos_de_matricula(self):
        """Teste que verifica os atributos do modelo de Matricula"""

        self.assertEqual(self.matricula.estudante, self.estudante_matricula)
        self.assertEqual(self.matricula.curso, self.curso_matricula)
        self.assertEqual(self.matricula.periodo, 'M')