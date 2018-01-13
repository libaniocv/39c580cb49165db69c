# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render,redirect
from . import models
from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm
from . import forms
from django.contrib.auth import authenticate,login
import django.forms as django_forms

# Create your views here.

#Pagina inicial
def index(request):
    u=[]
    c=[]
    if request.user.is_authenticated:
        # Obter usuario
        u = User.objects.get(pk=request.user.id)
        # Link com cliente
        try:
            c = models.Cliente.objects.get(user=u)
            print(c.foto_perfil)
        except:
            return redirect('/cadastro/etapa2/')


    context={
        'mensagem':'Pagina inicial',
        'cliente':c
    }

    return render(request,'p_index.html',context)

#Pagina cadastro e-mail e username
def cadastro1(request):
    u = []
    c = []
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method=='POST':
            form=forms.UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username=form.cleaned_data.get('username')
                raw_password=form.cleaned_data.get('password1')
                user1=authenticate(username=username,password=raw_password)
                login(request,user1)

                return redirect('/cadastro/etapa2/')
            else:
                return redirect('/cadastro/')
        else:
            form=forms.UserCreationForm()
            context={
                'form':form,
            }
            return render(request,'p_cadastro1.html',context)




#Pagina Verificaçao e-mail



#Página cadastro perfil informaçoes adicionais

def cadastro2(request):
    if request.method=='POST':
        usuario = User.objects.get(pk=request.user.id)
        cliente = models.Cliente(user=usuario)

        form=models.ClienteFormRegistro(request.POST,instance=cliente)

        if form.is_valid():

            form.save()
            return redirect('/')
        else:
            print(form.errors)
            return HttpResponse("Houve um erro no cadastro, tente novamente)")

    else:
        form=models.ClienteFormRegistro()
        context={
            'form':form
        }
        return render(request,'p_cadastro2.html',context)



#Pagina verificaçao de documentos


#Pagina login-aguardando confirmaçao e-mail



#Pagina Perfil



#Pagina editar perfil




##------Admin-----##
#Pagina Admin-inicio

#Pagina Admin-Verificar cadastros

#Pagina Admin-Responder suporte



##------Debug------##

def teste(request):
    context={}
    return render(request,'executive_default.html',context)