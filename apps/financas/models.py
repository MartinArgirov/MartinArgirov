from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='uploads_categorias', default='default_categoria.jpg')

    def __str__(self):
        return self.nome

class Despesa(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    descricao = models.CharField(max_length=50)
    valor = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
      return f'{self.descricao} - {self.valor} €'