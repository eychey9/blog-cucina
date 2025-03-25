from django.contrib import admin
from .models import Categoria, Articolo, Commento

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug')
    prepopulated_fields = {'slug': ('nome',)}

@admin.register(Articolo)
class ArticoloAdmin(admin.ModelAdmin):
    list_display = ('titolo', 'slug', 'autore', 'data_pubblicazione', 'categoria')
    list_filter = ('data_pubblicazione', 'categoria', 'autore')
    search_fields = ('titolo', 'contenuto')
    prepopulated_fields = {'slug': ('titolo',)}
    date_hierarchy = 'data_pubblicazione'
    ordering = ('data_pubblicazione',)

@admin.register(Commento)
class CommentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'articolo', 'data_creazione', 'attivo')
    list_filter = ('attivo', 'data_creazione')
    search_fields = ('nome', 'email', 'testo')
    actions = ['approva_commenti']
    
    def approva_commenti(self, request, queryset):
        queryset.update(attivo=True)
    approva_commenti.short_description = 'Approva commenti selezionati'
