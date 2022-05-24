from rest_framework import serializers
from .models import *

class AssinaturaSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Assinatura
        fields = '__all__'

class UsuariosGETSerializer(serializers.ModelSerializer):
    assinatura_FK = AssinaturaSerializer(read_only=True)
    class Meta:
        many = True
        model = Usuarios
        fields = '__all__'

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Usuarios
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Categoria
        fields = '__all__'

class FilmeGETSerializer(serializers.ModelSerializer):
    categoria_FK = CategoriaSerializer(read_only=True)
    class Meta:
        many = True
        model = Filmes
        fields = '__all__'

class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Filmes
        fields = '__all__'

class FavoritoGETSerializer(serializers.ModelSerializer):
    filme_FK = FilmeSerializer(read_only=True)
    usuario_FK = UsuariosSerializer(read_only=True)
    class Meta:
        many = True
        model = Favoritos
        fields = '__all__'

class FavoritoSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Favoritos
        fields = '__all__'