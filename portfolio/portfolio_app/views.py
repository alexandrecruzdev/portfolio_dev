from django.shortcuts import render
from django.http import HttpResponse
from .models import Habilidade,Projeto,Contato
# Create your views here.
def index(request):
    habilidades = Habilidade.objects.all()
    projetos = Projeto.objects.all()
    contatos = Contato.objects.all()

    context = {'habilidades':habilidades,'projetos':projetos,'contatos':contatos}
    return render(request,'index.html',context)