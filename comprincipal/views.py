# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render,redirect
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login

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
            form=UserCreationForm(request.POST)
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
            form=UserCreationForm()
            print(dir(form))
            context={
                'form':form,
            }
            return render(request,'p_cadastro1.html',context)




#Pagina Verificaçao e-mail



#Página cadastro perfil informaçoes adicionais

def cadastro2(request):
    return HttpResponse("Em construçao")


#Pagina verificaçao de documentos


#Pagina login-aguardando confirmaçao e-mail



#Pagina Perfil



#Pagina editar perfil




##------Admin-----##
#Pagina Admin-inicio

#Pagina Admin-Verificar cadastros

#Pagina Admin-Responder suporte



##------Debug------##