# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from . import models
from . import forms
from django.contrib.auth import authenticate, login
import django.forms as django_forms


# Create your views here.

# Pagina inicial
def index(request):
    u = []
    c = []
    if request.user.is_authenticated:
        # Obter usuario
        u = User.objects.get(pk=request.user.id)
        # Link com cliente
        try:
            c = models.Cliente.objects.get(user=u)
            print(c.foto_perfil)
        except:
            return redirect('/cadastro/etapa2/')

        try:
            anuncios=models.Anuncio.objects.all()
        except:
            anuncios=[]

    context = {
        'mensagem': 'Pagina inicial',
        'cliente': c,
        'anuncios': anuncios
    }

    return render(request, 'p_index.html', context)


#Pagina cadastro e-mail e username
def cadastro1(request):
    u = []
    c = []
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            form = forms.UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user1 = authenticate(username=username, password=raw_password)
                login(request, user1)

                return redirect('/cadastro/etapa2/')
            else:
                return redirect('/cadastro/')
        else:
            form = forms.UserCreationForm()
            context = {
                'form': form,
            }
            return render(request, 'p_cadastro1.html', context)


#Pagina Verificaçao e-mail



#Página cadastro perfil informaçoes adicionais

def cadastro2(request):
    if request.method == 'POST':
        usuario = User.objects.get(pk=request.user.id)
        cliente = models.Cliente(user=usuario)

        form = models.ClienteFormRegistro(request.POST, instance=cliente)

        if form.is_valid():

            form.save()
            return redirect('/')
        else:
            print(form.errors)
            return HttpResponse("Houve um erro no cadastro, tente novamente)")

    else:
        form = models.ClienteFormRegistro()
        context = {
            'form': form
        }
        return render(request, 'p_cadastro2.html', context)


#Pagina verificaçao de documentos


#Pagina login-aguardando confirmaçao e-mail



#Pagina Perfil
#Pagina editar perfil
def verperfil(request):
    erros = []
    u = []
    c = []
    if request.user.is_authenticated:
        # Obter usuario
        u = User.objects.get(pk=request.user.id)
        # Link com cliente
        try:
            c = models.Cliente.objects.get(user=u)

        except:
            return redirect('/cadastro/etapa2/')

        if request.method == 'POST':
            usuario = User.objects.get(pk=request.user.id)
            cliente = models.Cliente.objects.get(user=usuario)
            form = models.ClienteFormRegistro(request.POST)

            try:
                c.nome = request.POST.get("nome")
                c.save()
            except:
                erros.append("Nome invalido")

            try:
                c.cpf = request.POST.get("cpf")
                c.save()
            except:
                erros.append("CPF inválido ou já registrado")

            try:
                c.telefone = request.POST.get("telefone")
                c.save()
            except:
                erros.append("Número inválido ou já registrado")
            print(request.POST.get("foto_perfil"))

            print(len(request.FILES))
            if len(request.FILES) == 0:
                pass
            else:
                form = models.ClienteFormRegistro(request.POST, request.FILES)
                temp = request.FILES.get('foto_perfil')
                c.foto_perfil = temp
                c.save()

            try:
                c.endereco = request.POST.get("endereco")
                c.save()
            except:
                erros.append("Não foi possível mudar o endereço")

            return redirect('Perfil')



        else:

            form = models.ClienteFormRegistro()
            context = {
                'cliente': c,
                'form': form
            }

            return render(request, 'p_verperfil.html', context)
    else:
        return redirect('/login/')


#Pagina criar anuncio
def criaranuncio(request):
    erros = []
    u = []
    c = []
    if request.user.is_authenticated:
        # Obter usuario
        u = User.objects.get(pk=request.user.id)
        # Link com cliente
        try:
            c = models.Cliente.objects.get(user=u)

        except:
            return redirect('/cadastro/etapa2/')

    try:
        an=models.Anuncio.objects.get(proprietario=c)
        print("Possui anuncio")
        print(an.pk)
        return redirect('/')
    except:
        print("Não possui anuncio")


    if request.method == 'POST':
        form=models.AnuncioForm(request.POST)
        #Deletar anuncio antigo
        try:
            models.Anuncio.objects.get(proprietario=c).delete()
        except:
            pass


        t_quantia=request.POST.get("quantia_reservada")
        t_cotacao=request.POST.get("cotacao")
        t_descricao=request.POST.get("descricao")
        t_minimo=request.POST.get("minimo")
        t_maximo=request.POST.get("maximo")
        t_metodos=request.POST.getlist('metodos')

        novo_anuncio=models.Anuncio()
        novo_anuncio.proprietario=c
        novo_anuncio.quantia_reservada=t_quantia
        novo_anuncio.cotacao=t_cotacao
        novo_anuncio.descricao=t_descricao
        novo_anuncio.minimo=t_minimo
        novo_anuncio.maximo=t_maximo




        novo_anuncio.save()
        anuncio_criado=models.Anuncio.objects.get(proprietario=c)
        print(t_metodos)
        for i in t_metodos:
           print(int(i))
           anuncio_criado.metodos.add(i)





        return redirect('CriarAnuncio')
    else:
        form = models.AnuncioForm()
        context = {
            'form': form,
            'cliente': c
        }

        return render(request, 'p_novoanuncio.html', context)

#Pagina Detalhes anuncio
def veranuncio(request,anuncioid):
    erros = []
    u = []
    c = []
    if request.user.is_authenticated:
        # Obter usuario
        u = User.objects.get(pk=request.user.id)
        # Link com cliente
        try:
            c = models.Cliente.objects.get(user=u)

        except:
            return redirect('/cadastro/etapa2/')

    #Pegar anuncio
    try:
        a=models.Anuncio.objects.get(pk=anuncioid)
    except:
        erro="Anúncio não existe"
        return HttpResponse(erro)

    context={
        'cliente':c,
        'anuncio':a
    }

    return render(request,'p_veranuncio.html',context)


##------Admin-----##
#Pagina Admin-inicio

#Pagina Admin-Verificar cadastros

#Pagina Admin-Responder suporte



##------Debug------##

def teste(request):
    try:
        thread.start_new_thread(th_teste(request.user.id))
        return HttpResponse("iniciado")
    except:
        return HttpResponse("Não foi possivel criar thread")

