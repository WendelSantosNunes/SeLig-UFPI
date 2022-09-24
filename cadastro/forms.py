from datetime import date
from wsgiref.validate import validator
from xml.dom import ValidationErr

from conta.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

# from django.core.validators import validate_email


class UsuarioForm(UserCreationForm):

    data_nasc = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': "date"}
        )
    )

    def clean_email(self):
        nome, dominio = self.cleaned_data['email'].rsplit('@', 1)

        if dominio == 'ufpi.edu.br':
            return self.cleaned_data['email']
        else:
            raise ValidationErr('Necessário um Email institucional UFPI!')

    def clean_data_nasc(self):
        data = self.cleaned_data['data_nasc']
        atual = date.today()

        if int((atual - data).days) >= 5475:
            return self.cleaned_data['data_nasc']
        else:
            raise ValidationErr('erro')

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']

        if len(cpf) == 14:
            cpf_dig = cpf[0]+cpf[1]+cpf[2]+cpf[4]+cpf[5] + \
                cpf[6]+cpf[8]+cpf[9]+cpf[10]+cpf[12]+cpf[13]
            if cpf_dig.isdigit() and cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-':
                return self.cleaned_data['cpf']
        raise ValidationErr('CPF inválido!')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1',
                  'password2', 'img', 'cpf', 'curso', 'data_nasc']

        widgets = {
            'username': forms.TextInput(attrs={"placeholder": 'Digite seu nome do usuário'}),
            'first_name': forms.TextInput(attrs={"placeholder": 'Digite seu nome'}),
            'last_name': forms.TextInput(attrs={"placeholder": 'Digite seu sobrenome'}),
            'email': forms.TextInput(attrs={"placeholder": 'Digite seu email UFPI'}),
            'cpf': forms.TextInput(attrs={"placeholder": 'XXX-XXX-XXX-XX'}),
            'password1': forms.TextInput(attrs={"placeholder": 'Digite sua senha'}),
            'password2': forms.TextInput(attrs={"placeholder": 'Digite sua senha novamente'}),
        }
