# from select import select

from django.core.mail import send_mail
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from publicacao.models import Publicacao

# Create your views here.


def send_gmail(request, pk):
    if request.method == "POST":
        mensagem = request.POST.get('mensagem')
        motivo = request.POST.get('reasons')

        exemplo = Publicacao.objects.filter(id=pk).values()

        print(exemplo[0]['titulo'], motivo)

        mensagem_enviar = 'Descrição da denúncia: {}  Id do publicação: {} '.format(
            mensagem, pk)

        # mensagem_enviar = render_to_string(
        #     'senha/password_reset_email1.html'),

        send_mail(
            'Denúncia',
            mensagem_enviar,
            'seliga.ufpi@gmail.com',
            ['wendelnunes9999@gmail.com'],
            fail_silently=False,
        )

    return render(request, 'denuncia/denuncia.html')
