from django.db import models


class Pessoas(models.Model):
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.nome