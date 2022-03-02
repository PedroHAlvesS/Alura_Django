from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receitas


def dashboard(request):
    if request.user.is_authenticated:
        pessoa = request.user.id
        receitas_do_usuario = Receitas.objects.order_by('-data_receita').filter(publicado_por=pessoa)

        dados = {
            'receitas': receitas_do_usuario
        }

        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')


def logout(request):
    auth.logout(request)
    return redirect('index')


def login(request):
    # redirect the user if he's logged
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        email = request.POST['email'].strip()
        senha = request.POST['senha'].strip()
        if email == "" or senha == "":
            messages.error(request, "Campos não podem ser vazios!")
            return redirect(login)
        else:
            if User.objects.filter(email=email).exists():
                nome = User.objects.filter(email=email).values_list('username', flat=True).get()
                user = auth.authenticate(request, username=nome, password=senha)
                if user is not None:
                    auth.login(request, user)
                    messages.success(request, "logado com sucesso!")
                    return redirect(dashboard)
                else:
                    messages.error(request, "Erro ao logar!")
                    return redirect(login)
            else:
                messages.error(request, "Usuário não encontrado!")
                return redirect(login)
    return render(request, 'usuarios/login.html')


def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome'].strip()
        email = request.POST['email'].strip()
        senha = request.POST['password'].strip()
        senha_confirmacao = request.POST['password2'].strip()
        if not nome:
            messages.error(request, "Campo nome vazio!")
            return redirect(cadastro)
        elif not email:
            messages.error(request, "Campo email vazio!")
            return redirect(cadastro)
        elif not senha:
            messages.error(request, "Campo senha vazia!")
            return redirect(cadastro)
        elif not senha_confirmacao:
            messages.error(request, "Campo senha de confirmação vazia!")
            return redirect(cadastro)
        elif senha != senha_confirmacao:
            messages.error(request, "Senhas diferentes!")
            return redirect(cadastro)
        else:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Usuário já cadastrado')
                return redirect('cadastro')
            user = User.objects.create_user(username=nome, email=email, password=senha)
            user.save()
            messages.success(request, 'Usuário cadastrado com sucesso')
            return redirect(login)
    else:
        return render(request, 'usuarios/cadastro.html')


def criar_receita(request):
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']
        usuario = get_object_or_404(User, pk=request.user.id)
        nova_receita = Receitas(nome_da_receita=nome_receita, ingredientes=ingredientes, modo_de_preparo=modo_preparo,
                                tempo_de_preparo=tempo_preparo, rendimento=rendimento, categoria=categoria,
                                foto_da_receita=foto_receita, publicado_por=usuario)
        nova_receita.save()
        return redirect('dashboard')
    return render(request, 'usuarios/criar_receita.html')
