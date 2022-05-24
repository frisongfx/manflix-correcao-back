from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated


class UsuariosAPIView(APIView):
# permission_classes = (IsAuthenticated,)

    def get(self, request, pk=''):
        if 'nome' in request.GET:
            statusNome = request.GET['nome']
            usuarios = Usuarios.objects.filter(nome__contains=statusNome)
            serializer = UsuariosGETSerializer(usuarios, many=True)
            return Response(serializer.data)
        elif 'user' in request.GET:
            statusUser = request.GET['user']
            usuarios = Usuarios.objects.filter(idUserFK=statusUser)
            serializer = UsuariosGETSerializer(usuarios, many=True)
            return Response(serializer.data)
        elif 'assinatura' in request.GET:
            statusAssinatura = request.GET['assinatura']
            usuarios = Usuarios.objects.filter(idAssinaturaFK=statusAssinatura)
            serializer = UsuariosGETSerializer(usuarios, many=True)
            return Response(serializer.data)
        elif pk == '':
            usuarios = Usuarios.objects.all()
            serializer = UsuariosGETSerializer(usuarios, many=True)
            return Response(serializer.data)
        else:
            usuarios = Usuarios.objects.get(id=pk)
            serializer = UsuariosGETSerializer(usuarios)
            return Response(serializer.data)

    def post(self, request):
        serializer = UsuariosSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
        #return Response({"id": serializer.data['id']})

    def put(self, request, pk=''):
        usuarios = Usuarios.objects.get(id=pk)
        serializer = UsuariosSerializer(usuarios, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):        
        usuarios = Usuarios.objects.get(id=pk)       
        usuarios.delete()
        return Response({"msg": "Apagado com sucesso"})

class AssinaturaAPIView(APIView):
# permission_classes = (IsAuthenticated,)

    def get(self, request, pk=''):
        if 'nome' in request.GET:
            statusNome = request.GET['nome']
            assinaturas = Assinatura.objects.filter(nome__contains=statusNome)
            serializer = AssinaturaSerializer(assinaturas, many=True)
            return Response(serializer.data)
        elif pk == '':
            assinaturas = Assinatura.objects.all()
            serializer = AssinaturaSerializer(assinaturas, many=True)
            return Response(serializer.data)
        else:
            assinaturas = Assinatura.objects.get(id=pk)
            serializer = AssinaturaSerializer(assinaturas)
            return Response(serializer.data)

    def post(self, request):
        serializer = AssinaturaSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
        #return Response({"id": serializer.data['id']})

    def put(self, request, pk=''):
        assinaturas = Assinatura.objects.get(id=pk)
        serializer = AssinaturaSerializer(assinaturas, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):        
        assinaturas = Assinatura.objects.get(id=pk)       
        assinaturas.delete()
        return Response({"msg": "Apagado com sucesso"})

class CategoriaAPIView(APIView):
# permission_classes = (IsAuthenticated,)

    def get(self, request, pk=''):
        if 'nome' in request.GET:
            statusNome = request.GET['nome']
            categorias = Categoria.objects.filter(nome__contains=statusNome)
            serializer = CategoriaSerializer(categorias, many=True)
            return Response(serializer.data)
        elif pk == '':
            categorias = Categoria.objects.all()
            serializer = CategoriaSerializer(categorias, many=True)
            return Response(serializer.data)
        else:
            categorias = Categoria.objects.get(id=pk)
            serializer = CategoriaSerializer(categorias)
            return Response(serializer.data)

    def post(self, request):
        serializer = CategoriaSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
        #return Response({"id": serializer.data['id']})

    def put(self, request, pk=''):
        categorias = Categoria.objects.get(id=pk)
        serializer = CategoriaSerializer(categorias, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):        
        categorias = Categoria.objects.get(id=pk)       
        categorias.delete()
        return Response({"msg": "Apagado com sucesso"})

class FilmesAPIView(APIView):
# permission_classes = (IsAuthenticated,)

    def get(self, request, pk=''):
        if 'nome' in request.GET:
            statusNome = request.GET['nome']
            filmes = Filmes.objects.filter(nome__contains=statusNome)
            serializer = FilmeGETSerializer(filmes, many=True)
            return Response(serializer.data)
        elif 'categoria' in request.GET:
            statusCategoria = request.GET['categoria']
            filmes = Filmes.objects.filter(categoria_FK=statusCategoria)
            serializer = FilmeGETSerializer(filmes, many=True)
            return Response(serializer.data)
        elif pk == '':
            filmes = Filmes.objects.all()
            serializer = FilmeGETSerializer(filmes, many=True)
            return Response(serializer.data)
        else:
            filmes = Filmes.objects.get(id=pk)
            serializer = FilmeGETSerializer(filmes)
            return Response(serializer.data)

    def post(self, request):
        serializer = FilmeSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
        #return Response({"id": serializer.data['id']})

    def put(self, request, pk=''):
        filmes = Filmes.objects.get(id=pk)
        serializer = FilmeSerializer(filmes, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):        
        filmes = Filmes.objects.get(id=pk)       
        filmes.delete()
        return Response({"msg": "Apagado com sucesso"})

class FavoritosAPIView(APIView):
# permission_classes = (IsAuthenticated,)

    def get(self, request, pk=''):
        if 'filme' in request.GET:
            statusFilme = request.GET['filme']
            favoritos = Favoritos.objects.filter(filme_FK=statusFilme)
            serializer = FavoritoGETSerializer(favoritos, many=True)
            return Response(serializer.data)
        elif 'usuario' in request.GET:
            statusUsuario = request.GET['usuario']
            favoritos = Favoritos.objects.filter(usuario_FK=statusUsuario)
            serializer = FavoritoGETSerializer(favoritos, many=True)
            return Response(serializer.data)
        elif pk == '':
            favoritos = Favoritos.objects.all()
            serializer = FavoritoGETSerializer(favoritos, many=True)
            return Response(serializer.data)
        else:
            favoritos = Favoritos.objects.get(id=pk)
            serializer = FavoritoGETSerializer(favoritos)
            return Response(serializer.data)

    def post(self, request):
        serializer = FavoritoSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
        #return Response({"id": serializer.data['id']})

    def put(self, request, pk=''):
        favoritos = Favoritos.objects.get(id=pk)
        serializer = FavoritoSerializer(favoritos, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):        
        favoritos = Favoritos.objects.get(id=pk)       
        favoritos.delete()
        return Response({"msg": "Apagado com sucesso"})