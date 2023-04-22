from django.contrib import admin
from django import forms

from apps.loja.forms import EnderecoForm
from apps.loja.models import Cliente, ClienteEndereco


class ClienteEnderecoForm(forms.ModelForm):
    cep = forms.CharField(label="Cep", max_length=100)
    logradouro = forms.CharField(max_length=100)
    bairro = forms.CharField(max_length=100)
    localidade = forms.CharField(max_length=100)
    numero = forms.CharField(max_length=100)
    titulo = forms.CharField(max_length=100)

    class Meta:
        model = ClienteEndereco
        fields = (
            'default',
        )

    def __init__(self, *args, **kwargs):
        super(ClienteEnderecoForm, self).__init__(*args, **kwargs)
        if self.instance.cod_endereco:
            self.fields['cep'].initial = self.instance.cod_endereco.cep
            self.fields['logradouro'].initial = self.instance.cod_endereco.logradouro
            self.fields['bairro'].initial = self.instance.cod_endereco.bairro
            self.fields['localidade'].initial = self.instance.cod_endereco.localidade
            self.fields['numero'].initial = self.instance.cod_endereco.numero
            self.fields['titulo'].initial = self.instance.cod_endereco.titulo

    def clean(self):
        cleaned_data = super().clean()
        endereco_data = cleaned_data
        endereco_data.pop('default')
        endereco_data.pop('cod_cliente')
        endereco_form = EnderecoForm(data=endereco_data)
        if not endereco_form.is_valid():
            raise forms.ValidationError(f'Erro ao salvar o endereço: {endereco_form.errors.as_text()}')
        endereco = endereco_form.save(commit=False)
        if endereco:
            endereco.save()
            self.instance.cod_endereco = endereco
        return cleaned_data


class ClienteEnderecoInline(admin.StackedInline):
    model = ClienteEndereco
    form = ClienteEnderecoForm
    extra = 1


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'cpf',
        'email',
    )
    inlines = [ClienteEnderecoInline]