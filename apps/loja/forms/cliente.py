from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from apps.loja.models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = (
            'nome',
            'cpf',
            'email'
        )
