from django.contrib import admin
from .models import *

class detUsuarios(admin.ModelAdmin):
    list_display = ('id','nome', 'email', 'fone')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Usuarios, detUsuarios)

class detAssinatura(admin.ModelAdmin):
    list_display = ('id','nome', 'valor')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Assinatura, detAssinatura)

class detCategoria(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Categoria, detCategoria)

class detFilmes(admin.ModelAdmin):
    list_display = ('id','nome', 'foto', 'banner', 'logo', 'descricao')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Filmes, detFilmes)

class detFavoritos(admin.ModelAdmin):
    list_display = ('id','usuario_FK', 'filme_FK')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Favoritos, detFavoritos)