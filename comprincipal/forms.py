# -*- coding: utf-8 -*-
from . import models
from django.forms import ModelForm

def FormCadastro1(ModelForm):
    class Meta:
        model=models.Cliente