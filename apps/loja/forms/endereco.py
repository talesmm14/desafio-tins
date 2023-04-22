from django import forms
from django.forms import inlineformset_factory

from apps.loja.models import Endereco, ClienteEndereco, Cliente


class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = (
            'cep',
            'logradouro',
            'bairro',
            'localidade',
            'numero',
            'titulo',
        )


class ClienteEnderecoForm(forms.ModelForm):
    cep = forms.CharField(max_length=9)
    numero = forms.IntegerField()
    titulo = forms.CharField(max_length=100)

    class Meta:
        model = ClienteEndereco
        fields = (
            'cep',
            'numero',
            'titulo',
            'default',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.cod_endereco:
            self.fields['cep'].initial = self.instance.cod_endereco.cep
            self.fields['logradouro'].initial = self.instance.cod_endereco.logradouro
            self.fields['bairro'].initial = self.instance.cod_endereco.bairro
            self.fields['localidade'].initial = self.instance.cod_endereco.localidade
            self.fields['numero'].initial = self.instance.cod_endereco.numero
            self.fields['titulo'].initial = self.instance.cod_endereco.titulo

    def save(self, commit=True):
        endereco = self.instance.cod_endereco or Endereco()
        endereco.cep = self.cleaned_data['cep']
        endereco.numero = self.cleaned_data['numero']
        endereco.titulo = self.cleaned_data['titulo']
        endereco.save()

        cliente_endereco = super().save(commit=False)
        cliente_endereco.cod_endereco = endereco
        if commit:
            cliente_endereco.save()
        return cliente_endereco


ClienteEnderecoFormSet = inlineformset_factory(
    Cliente,
    ClienteEndereco,
    form=ClienteEnderecoForm,
    extra=5,
    can_delete=True,
)
