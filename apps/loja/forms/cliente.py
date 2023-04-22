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
