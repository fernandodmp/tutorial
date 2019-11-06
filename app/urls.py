from django.urls import path

from .views import view_app, lista_usuarios, lista_usuarios_v2, message, cria_usuario

urlpatterns = [
    path('caminho/', view_app, name="view"),
    path('users/', lista_usuarios, name="users"),
    path('users/v2/', lista_usuarios_v2, name="users_v2"),
    path('message/', message, name ="message"),
    path('users/new', cria_usuario, name="cria_user")
]