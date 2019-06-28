from django.urls import path
from .views import index, listar_pessoas, cadastrar_pessoa, \
                   alterar_pessoa, deletar_pessoa

urlpatterns = [
    path('home', index),
    path('lista',  listar_pessoas, name='listar'),
    path('nova',   cadastrar_pessoa, name='cadastrar'),
    path('altera/<int:id>',  alterar_pessoa,  name='alterar'),
    path('deleta/<int:id>', deletar_pessoa, name='deletar')
]