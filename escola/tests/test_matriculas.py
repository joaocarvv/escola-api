from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculaCursoSerializer



class EstudantesTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Matriculas-list')
        self.client.force_authenticate(user=self.user)
        self.estudante = Estudante.objects.create(
                nome = 'Estudante Teste',
                email = 'estudante@gmail.com',
                cpf = '77567543010',
                data_nascimento = '2023-01-01',
                celular = '11 99999-9999',
        )
        self.curso = Curso.objects.create(
                codigo = 'POO',
                descricao = 'Programação Orientada a Objetos',
                nivel = 'B',
        )
        self.matricula = Matricula.objects.create(
                estudante = self.estudante,
                curso = self.curso,
                periodo = 'M',
        )
       
    def test_requisicao_get_para_listar_matriculas(self):
        """Teste para verificar a requisição GET para listar as matriculas"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_para_listar_um_matricula(self):
        """Teste para verificar a requisição GET para listar um matricula"""
        response = self.client.get(self.url+'1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)  
        dados_matricula = Matricula.objects.get(pk=1)
        dados_matricula_serializados = MatriculaSerializer(instance=dados_matricula).data
        self.assertEqual(response.data, dados_matricula_serializados)

    def test_requisicao_post_para_criar_matriculas(self):
        """Teste para verificar a requisição POST para um matricula"""
        dados = {
            'estudante': self.estudante.pk,
            'curso': self.curso.pk,
            'periodo': 'M',
        }
        response = self.client.post(self.url, dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_requisicao_delete_uma_matricula(self):
        """Teste de requisição DELETE uma matricula"""
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_requisicao_put_para_atualizar_matricula(self):
        """Teste de requisição PUT para uma matricula"""
        dados = {
            'estudante': self.estudante.pk,
            'curso': self.curso.pk,
            'periodo': 'M',
        }
        response = self.client.put(f'{self.url}1/', dados)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        
        