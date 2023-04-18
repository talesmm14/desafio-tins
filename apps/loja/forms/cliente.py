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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar', css_class='btn-primary', type='submit'))
