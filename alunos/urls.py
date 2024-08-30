from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro_aluno, name='cadastro_aluno'),
    path('listar/', views.lista_alunos, name='listar_alunos'),
]