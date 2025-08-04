from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante
from escola.serializers import EstudanteSerializer



class EstudantesTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Estudantes-list')
        self.client.force_authenticate(user=self.user)
        self.estudante_01 = Estudante.objects.create(
            nome = 'Teste estudante UM',
            email = 'testedeserializer01@gmail.com',
            cpf = '01119001072',
            data_nascimento = '2023-01-01',
            celular = '86 99999-9999',
        )
        self.estudante_02 = Estudante.objects.create(
            nome = 'Teste estudante DOIS',
            email = 'testedeserializer02@gmail.com',
            cpf = '15862474099',
            data_nascimento = '2023-01-01',
            celular = '86 99999-9999',
        )
    def test_requisicao_get_para_listar_estudantes(self):
        """Teste para verificar a requisição GET para listar os estudantes"""
        response = self.client.get(self.url)#/estudantes/
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_requisicao_get_para_listar_um_estudantes(self):
        """Teste para verificar a requisição GET para listar um estudantes"""
        response = self.client.get(self.url+'1/')#/estudantes/1/
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_estudante = Estudante.objects.get(pk=1)
        dados_estudante_serializados = EstudanteSerializer(instance=dados_estudante).data
        self.assertEqual(response.data, dados_estudante_serializados)
    
    def test_requisicao_post_para_criar_estudantes(self):
        """Teste para verificar a requisição POST para um estudantes"""
        dados = {
            'nome': 'testea',
            'email': 'testedeserializer03@gmail.com',
            'cpf': '60936994045',
            'data_nascimento': '2023-01-01',
            'celular': '54 99999-9999',
        }
        response = self.client.post(self.url, dados, format='json')

        
    def test_requisicao_delete_um_estudantes(self):
        """Teste de requisição DELETE um estudantes"""
        response = self.client.delete(f'{self.url}2/')#/estudantes/2/
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_put_para_atualizar_estudantes(self):
        """Teste de requisição PUT para um estudante"""
        dados = {
            'nome': 'testeput',
            'email': 'testeput@gmail.com',
            'cpf': '01119001072',
            'data_nascimento': '2023-01-01',
            'celular': '22 99999-9999',
        }
        response = self.client.put(f'{self.url}1/', dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)