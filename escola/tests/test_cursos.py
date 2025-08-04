from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Curso
from escola.serializers import CursoSerializer




class CursosTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Cursos-list')
        self.client.force_authenticate(user=self.user)
        self.curso_01 = Curso.objects.create(
            codigo = 'POO',
            descricao = 'Programação Orientada a Objetos',
            nivel = 'B',
        )
        self.curso_02 = Curso.objects.create(
            codigo = 'IPA',
            descricao = 'Introdução à Programação',
            nivel = 'B',
        )
    def test_requisicao_get_para_listar_cursos(self):
        """Teste para verificar a requisição GET para listar os cursos"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_para_listar_um_curso(self):
        """Teste para verificar a requisição GET para listar um curso"""
        response = self.client.get(self.url+'1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_curso = Curso.objects.get(pk=1)
        dados_curso_serializados = CursoSerializer(instance=dados_curso).data
        self.assertEqual(response.data, dados_curso_serializados)

    def test_requisicao_post_para_criar_cursos(self):
        """Teste para verificar a requisição POST para um curso"""
        dados = {
            'codigo': 'DUP',
            'descricao': 'Programação Orientada',
            'nivel': 'B',
    }
        response = self.client.post(self.url, dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_requisicao_delete_um_curso(self):
        """Teste de requisição DELETE um curso"""
        response = self.client.delete(f'{self.url}2/')#/curso/2/
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_put_para_atualizar_curso(self):
        """Teste de requisição PUT para um curso"""
        dados = {
            'codigo': 'BOB',
            'descricao': 'Programação Oriente',
            'nivel': 'B',
        }
        response = self.client.put(f'{self.url}1/', dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)  