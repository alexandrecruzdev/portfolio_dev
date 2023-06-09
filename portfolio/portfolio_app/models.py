from django.db import models

# Create your models here.

class Habilidade(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='upload/habilidade/')
    

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    url = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='upload/projetos/')
    

    def __str__(self):
        return self.url


class Contato(models.Model):
    contato = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='upload/contatos/')
    link = models.CharField(max_length=100, default='')
    

    def __str__(self):
        return self.contato
        
