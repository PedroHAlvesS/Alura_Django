from django.contrib import admin
from .models import Receitas

# Register your models here.


class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_da_receita', 'categoria', 'publicado_por', 'publicar')
    list_display_links = ('id', 'nome_da_receita',)
    search_fields = ('nome_da_receita',)
    list_filter = ('categoria', 'publicar')
    list_editable = ('publicar',)
    list_per_page = 6


admin.site.register(Receitas, ListandoReceitas)
