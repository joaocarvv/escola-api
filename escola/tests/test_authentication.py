from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status



class AuthenticationTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Estudantes-list')
        

    def test_autenticacao_user_com_credenciais_corretas(self):
        """Teste que verifica a autenticação de um usuário com credenciais corretas"""
        user = authenticate(username='admin', password='admin')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_autenticacao_user_com_username_incorreto(self):
        """Teste que verifica a autenticação de um usuário com username incorreto"""
        user = authenticate(username='admn', password='admin')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_autenticacao_user_com_senha_incorreta(self):
        """Teste que verifica a autenticação de um usuário com senha incorreta"""
        user = authenticate(username='admin', password='adm')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_requisicao_get_autorizada(self):
        """Teste que verifica uma requisição GET autorizada"""
        self.client.force_authenticate(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)



    