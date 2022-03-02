from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.


class Receitas(models.Model):
    publicado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_da_receita = models.CharField(max_length=180)
    ingredientes = models.TextField()
    modo_de_preparo = models.TextField()
    tempo_de_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateTimeField(default=datetime.now(), blank=True)
    foto_da_receita = models.ImageField(upload_to='fotos/%d/%m/%Y', blank=True)
    publicar = models.BooleanField(default=False)

    objects = models.Manager()

    class Meta:
        verbose_name = "Receita"
        verbose_name_plural = "Receitas"

    def __str__(self):
        return self.nome_da_receita
