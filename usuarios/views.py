from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'usuarios/dashboard.html')
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
            print("Campos não podem ser vazios!")
            return redirect(login)
        else:
            if User.objects.filter(email=email).exists():
                nome = User.objects.filter(email=email).values_list('username', flat=True).get()
                user = auth.authenticate(request, username=nome, password=senha)
                if user is not None:
                    auth.login(request, user)
                    print("logado com sucesso!")
                    return redirect(dashboard)
                else:
                    print("Erro ao logar!")
                    return redirect(login)
    return render(request, 'usuarios/login.html')


def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome'].strip()
        email = request.POST['email'].strip()
        senha = request.POST['password'].strip()
        senha_confirmacao = request.POST['password2'].strip()
        if not nome:
            print("Campo nome vazio!")
            return redirect(cadastro)
        elif not email:
            print("Campo email vazio!")
            return redirect(cadastro)
        elif not senha:
            print("Campo senha vazia!")
            return redirect(cadastro)
        elif not senha_confirmacao:
            print("Campo senha de confirmação vazia!")
            return redirect(cadastro)
        elif senha != senha_confirmacao:
            print("Senhas diferentes!")
            return redirect(cadastro)
        else:
            if User.objects.filter(email=email).exists():
                print('Usuário já cadastrado')
                return redirect('cadastro')
            user = User.objects.create_user(username=nome, email=email, password=senha)
            user.save()
            print('Usuário cadastrado com sucesso')
            return redirect(login)
    else:
        return render(request, 'usuarios/cadastro.html')
