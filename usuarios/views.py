from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def dashboard(request):
    pass


def logout(request):
    pass


def login(request):
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
