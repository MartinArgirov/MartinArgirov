from django.urls import path
from .views import (home, about, CategoriaCreateView, CategoriaDetailView, CategoriaListView, CategoriaUpdateView,
                    DespesaCreateView, DespesaDetailView, DespesaListView, DespesaUpdateView, CarroQuery, LivroQuery)

app_name = "financas"

urlpatterns = [
    path('', home, name='home'),
    path('', about, name='about'),
    path('categorias/new', CategoriaCreateView.as_view(), name='categoria-new'),
    path('categorias/list', CategoriaListView.as_view(), name='categoria-list'),
    path('categorias/update/<int:pk>', CategoriaUpdateView.as_view(), name='categoria-update'),
    path('categorias/detail/<int:pk>', CategoriaDetailView.as_view(), name='categoria-detail'),
    path('despesas/new', DespesaCreateView.as_view(), name='despesa-new'),
    path('despesas/list', DespesaListView.as_view(), name='despesa-list'),
    path('despesas/update/<int:pk>', DespesaUpdateView.as_view(), name='despesa-update'),
    path('despesas/detail/<int:pk>', DespesaDetailView.as_view(), name='despesa-detail'),
    path('despesas/list/carro', CarroQuery.as_view(), name='despesa-list-carro'),
    path('despesas/list/livros', LivroQuery.as_view(), name='despesa-list-livro'),
]