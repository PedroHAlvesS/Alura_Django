from django.shortcuts import render, get_object_or_404
from.models import Receitas


def index(request):
    receitas_local = Receitas.objects.order_by('-data_receita').filter(publicar=True)

    dados = {
        'receitas': receitas_local
    }
    return render(request, 'index.html', dados)


def receita(request, receita_id):
    receita = get_object_or_404(Receitas, pk=receita_id)

    receita_a_exibir = {
        'receitas': receita
    }
    return render(request, 'receita.html', receita_a_exibir)


def buscar(request):
    dados = {
        'receitas': ''
    }
    if 'q' in request.GET:
        nome_da_procura = request.GET['q']
        if nome_da_procura:
            receita_busca = Receitas.objects.order_by('-data_receita').filter(publicar=True, nome_da_receita__icontains=nome_da_procura)
            dados['receitas'] = receita_busca
    return render(request, 'buscar.html', dados)
