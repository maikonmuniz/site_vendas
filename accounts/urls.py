from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('carrinho', views.carrinho, name='carrinho'),
    path('loja/cadastro', views.cadastro_loja, name='cadastro_loja'),
    path('loja/dashboard', views.dashboard_loja, name='dashboard_loja'),
    path('loja/cadastro_produto', views.cadastro_produto, name='cadastro_prod')
    #path('<string:username>/dados', views.editar_dados, name='editar_dados')
]
