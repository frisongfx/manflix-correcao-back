from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone

# impede a criação de usuários com emails repetidos
User._meta.get_field('email')._unique = True
#impede com que o email seja null ou vazio durante cadastro
User._meta.get_field('email').blank = False
User._meta.get_field('email').null = False

def upload_imagem_filme(instance, filename):
    return f"{instance.nome}-{filename}"

def upload_imagem_banner(instance, filename):
    return f"{instance.nome}-{filename}"

def upload_imagem_logo(instance, filename):
    return f"{instance.nome}-{filename}"

class Categoria(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome

class Filmes(models.Model):
    nome = models.CharField(max_length=150)
    categoria_FK = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to=upload_imagem_filme, blank=True, null=True)
    banner = models.ImageField(upload_to=upload_imagem_banner, blank=True, null=True)
    logo = models.ImageField(upload_to=upload_imagem_logo, blank=True, null=True)
    descricao = models.CharField(max_length=500, default=None)
    ano = models.CharField(max_length=4, default=None)
    temps = models.CharField(max_length=2, default=None)

    def __str__(self):
        return self.nome

class Assinatura(models.Model):
    nome = models.CharField(max_length=150)
    valor = models.FloatField()

    def __str__(self):
        return self.nome

class Usuarios(models.Model):
    nome = models.CharField(max_length=55)
    cpf = models.CharField(max_length=11, default=None)
    nasc = models.CharField(max_length=15, default=None)
    email = models.CharField(max_length=80)
    fone = models.CharField(max_length=15, null=True, blank=True)

    idUser_FK = models.ForeignKey(User, related_name="usuario", on_delete=models.CASCADE)
    assinatura_FK = models.ForeignKey(Assinatura, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return self.nome

class Favoritos(models.Model):
    filme_FK = models.ForeignKey(Filmes, on_delete=models.CASCADE)
    usuario_FK = models.ForeignKey(Usuarios, on_delete=models.CASCADE)