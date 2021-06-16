from django.shortcuts import render, redirect
from django.contrib import auth, messages
from .models import Usuario, Cliente, Loja
from django.conf import settings
import requests as req


# Create your views here.
def login(request):
    if request.method == 'POST':
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        result = req.post(url, data=values)
        result = result.json()
        if result['success']:
            email = request.POST['email']
            senha = request.POST['senha']
            user = auth.authenticate(request, username=email, password=senha)
            if user is not None:
                auth.login(request, user)
                if user.is_cliente:
                    return redirect('dashboard')
                else:
                    return redirect('dashboard_loja')
            else:
                messages.error(request, 'Email ou senha inválidos')
                return redirect('login')
        else:
            messages.error(request, 'Captcha inválido')
            return redirect('login')
    return render(request, 'login.html')


def cadastro(request):
    if request.method == 'POST':
        key = settings.SMS_SECRET_KEY
        nome = request.POST['nome']
        telefone = request.POST['telefone']
        email = request.POST['email']
        senha = request.POST['senha']
        if Usuario.objects.filter(email=email).exists():
            return redirect('cadastro')
        user = Usuario.objects.create_user(username=email,
                                           email=email,
                                           password=senha,
                                           is_cliente=True,
                                           first_name=nome,
                                           telefone=telefone)
        cliente = Cliente.objects.create(user=user)
        cliente.save()
        mensagem = 'Seu usuário foi cadastrado com sucesso'
        url_sms = 'https://api.smsdev.com.br/v1/send?key={}&type=9&msg={}&number={}'.format(key, mensagem, telefone)
        resp = req.get(url_sms)
        return redirect('login')
    return render(request, 'cadastro_usuario.html')


def cadastro_loja(request):
    if request.method == 'POST':
        nome_responsavel = request.POST['nome_responsavel']
        nome_loja = request.POST['nome_loja']
        endereco = request.POST['endereco']
        cidade = request.POST['cidade']
        cep = request.POST['cep']
        cnpj = request.POST['cnpj']
        email = request.POST['email']
        senha = request.POST['senha']
        if Usuario.objects.filter(email=email).exists():
            return redirect('cadastro_loja')
        user = Usuario.objects.create_user(username=email,
                                           email=email,
                                           password=senha,
                                           is_loja=True)
        loja = Loja.objects.create(user=user)
        loja.nome_responsavel = nome_responsavel
        loja.nome_loja = nome_loja
        loja.endereco = endereco
        loja.cidade = cidade
        loja.cep = cep
        loja.cnpj = cnpj
        loja.save()
        return redirect('login')
    return render(request, 'cadastro_loja.html')


def dashboard(request):
    if request.user.is_authenticated and request.user.is_cliente:
        return render(request, 'dashboard.html')
    else:
        return redirect('index')


def logout(request):
    auth.logout(request)
    return redirect('login')


def carrinho(request):
    if request.user.is_authenticated:
        return render(request, 'carrinho.html')
    else:
        return redirect('index')


def dashboard_loja(request):
    if request.user.is_authenticated and request.user.is_loja:
        return render(request, 'dashboard_loja.html')
    else:
        return redirect('index')


def cadastro_produto(request):
    pass


def editar_dados(request, username):
    if request.user.is_authenticated:
        if Usuario.objects.filter(first_name=username).exists:
            return render(request, 'dados_cliente.html')
    else:
        return redirect('index')
