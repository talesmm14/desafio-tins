from django.contrib import messages
from django.shortcuts import render, redirect

from apps.loja.forms import ClienteForm
from apps.loja.forms.endereco import ClienteEnderecoForm, EnderecoForm, ClienteEnderecoFormSet


def cadastro_cliente(request):
    form = ClienteForm()
    formset = ClienteEnderecoFormSet()
    return render(request, "cadastro_cliente.html", {"form": form, "formset": formset})
