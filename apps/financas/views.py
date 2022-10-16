from django.shortcuts import render
from django.db.models import Sum
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.urls import reverse_lazy
from .models import Categoria, Despesa

# Create your views here.
def home(request):
    categoria_carro = Categoria.objects.get(nome = 'Carro')
    valor_carro = Despesa.objects.filter(categoria__nome = 'Carro').aggregate(total=Sum('valor'))
    categoria_livros = Categoria.objects.get(nome = 'Livros')
    valor_livros = Despesa.objects.filter(categoria__nome = 'Livros').aggregate(total=Sum('valor'))
    return render(request, 'financas/home.html', context={'valor_carro':valor_carro, 'categoria_carro':categoria_carro, 'valor_livros':valor_livros, 'categoria_livros':categoria_livros})

class CategoriaCreateView(CreateView):
    model = Categoria
    fields = '__all__'
    success_url = reverse_lazy('financas:categoria-list')

class CategoriaListView(ListView):
    model = Categoria

class CategoriaUpdateView(UpdateView):
    model = Categoria    
    fields = '__all__'
    success_url = reverse_lazy('financas:categoria-list')

class CategoriaDetailView(DetailView):
    model = Categoria

class DespesaCreateView(CreateView):
    model = Despesa
    fields = '__all__'
    success_url = reverse_lazy('financas:despesa-list')

class DespesaListView(ListView):
    model = Despesa

    def get_context_data(self, **kwargs): 
        ctx = super().get_context_data(**kwargs)
        ctx['total'] = Despesa.objects.aggregate(a=Sum('valor'))
        return ctx

class DespesaUpdateView(UpdateView):
    model = Despesa    
    fields = '__all__'
    success_url = reverse_lazy('financas:despesa-list')

class DespesaDetailView(DetailView):
    model = Despesa

class CarroQuery(ListView):
    model = Despesa
    queryset = Despesa.objects.filter(categoria__nome='Carro')
    template_name = 'financas/despesa_list.html'

    def get_context_data(self, **kwargs): 
        ctx = super().get_context_data(**kwargs)
        ctx['total'] = Despesa.objects.filter(categoria__nome = 'Carro').aggregate(a=Sum('valor'))
        return ctx

class LivroQuery(ListView):
    model = Despesa
    queryset = Despesa.objects.filter(categoria__nome='Livros')
    template_name = 'financas/despesa_list.html'

    def get_context_data(self, **kwargs): 
        ctx = super().get_context_data(**kwargs)
        ctx['total'] = Despesa.objects.filter(categoria__nome = 'Livros').aggregate(a=Sum('valor'))
        return ctx
