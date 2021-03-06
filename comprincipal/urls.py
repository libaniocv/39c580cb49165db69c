"""sitexrb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'cadastro/$', views.cadastro1, name='Cadastro1'),
    url(r'cadastro/etapa2/$', views.cadastro2, name='Cadastro2'),
    url(r'teste/$', views.teste, name='teste'),
    url(r'perfil/$', views.verperfil, name='Perfil'),
    url(r'anuncio/novo/$', views.criaranuncio, name='CriarAnuncio'),
    url(r'anuncio/(?P<anuncioid>[0-9]+)/$', views.veranuncio, name='VerAnuncio'),

]
