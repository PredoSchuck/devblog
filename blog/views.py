from django.shortcuts import render
from .models import Artigo, Categoria

def home(request):
    noticias = Artigo.objects.all()
    categorias = Categoria.objects.all()

    contexto = {
        'lista_artigos': noticias,
        'lista_categorias': categorias
    }

    return render(request, 'blog/index.html', contexto)

def sobre_nos(request):
    return render(request, "blog/sobre.html")