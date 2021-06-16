from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Usuario(AbstractUser):
    is_cliente = models.BooleanField(default=False)
    is_loja = models.BooleanField(default=False)
    telefone = models.CharField(max_length=14, blank=True)


class Cliente(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)


class Loja(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    nome_responsavel = models.CharField(max_length=100)
    nome_loja = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=20)
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)


class Produto(models.Model):
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    image = models.ImageField(upload_to="img/%y", blank=True)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0)
