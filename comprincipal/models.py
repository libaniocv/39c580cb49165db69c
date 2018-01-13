# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import ModelForm


lista_status = (
    ('NV', 'Não Verificado'),
    ('V1', 'Verificado Level 1'),
    ('V2', 'Verificado Level 2')
)

#Nao utilizado por enquanto
lista_metodos=(
    ('BB', 'Banco do Brasil'),
    ('IT','ITAU'),
    ('CEF','Caixa Econômica'),
    ('SNT','Santander'),
    ('BRD','Bradesco')

)


# Create your models here.
class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11,unique=True)
    endereco = models.CharField(max_length=250)
    saldo = models.FloatField(default=0)
    carteira_xrb = models.CharField(max_length=250)
    telefone = models.CharField(max_length=250,unique=True)
    status_verificacao = models.CharField(max_length=200, choices=lista_status, default='NV')
    numero_transacoes = models.IntegerField(default=0)
    valor_transacoes = models.FloatField(default=0)
    reputacao = models.FloatField(default=0)
    login_email_token=models.CharField(max_length=50,default='Token')
    foto_perfil=models.ImageField(upload_to='perfil/',default='perfil/generico.png')

class ClienteFormRegistro(ModelForm):
    class Meta:
        model=Cliente
        fields=[
            'nome',
            'cpf',
            'endereco',
            'telefone',
        ]


class Anuncio(models.Model):
    proprietario = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    quantia_reservada=models.FloatField()
    cotacao=models.FloatField() #Valor em BRL para 1 XRB
    descricao=models.TextField()
    minimo=models.FloatField() #Em reais
    maximo=models.FloatField() #Em reais
    metodos=models.CharField(max_length=250) #Para manter pureza de código, iremos limitar as opções no front-end



class Representante(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    #Permissao
    permissao=models.IntegerField(default=0)
    # 0: Usuário comum
    # 1: Representante
    # 2: Administrador
