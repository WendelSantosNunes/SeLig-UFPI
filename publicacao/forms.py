from datetime import date
from xml.dom import ValidationErr

from django import forms

from .models import Publicacao


class PublicarForm(forms.ModelForm):
    pass
    data_evento = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': "date"}
        )
    )

    def clean_data_evento(self):
        data = self.cleaned_data['data_evento']
        atual = date.today()

        if int((data - atual).days) > 0:
            return self.cleaned_data['data_evento']
        else:
            raise ValidationErr('erro')

    class Meta:
        model = Publicacao

        fields = ['titulo', 'tipo', 'public', 'data_evento',
                  'img', 'local', 'custo', 'descricao']

        widgets = {
            'local': forms.TextInput(attrs={"placeholder": 'Picos'})
        }
