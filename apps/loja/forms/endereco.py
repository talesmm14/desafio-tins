from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.forms import inlineformset_factory

from apps.loja.forms import ClienteForm
from apps.loja.models import Endereco, ClienteEndereco, Cliente


class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = (
            'cep',
            'numero',
            'titulo',
        )


class ClienteEnderecoForm(forms.ModelForm):
    class Meta:
        model = ClienteEndereco
        fields = (
            'cod_endereco',
            'default',
        )


ClienteEnderecoFormSet = inlineformset_factory(
    Cliente,
    ClienteEndereco,
    form=ClienteEnderecoForm,
    extra=5,
    can_delete=True
)
