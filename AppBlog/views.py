
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy


from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
from AppBlog.models import *
from AppBlog.forms import *
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

# Create your views here.

def inicio(request): 
        return render(request, 'inicio.html')

def about(request): 
    return render(request, 'AppBlog/acerca.html')

def articulos(request): 
    return render(request, 'AppBlog/pages.html')


def detalle_articulo(request): 
    return render(request, 'AppBlog/detalle.html')

@login_required
def crear_articulo(request):
    if request.method=="POST":
        formulario=Formulario_Articulo(request.POST)
        
        if formulario.is_valid(): 
           data = formulario.cleaned_data
           titulo=data['titulo']
           subtitulo=data['subtitulo']
           cuerpo=data['cuerpo']
           fecha=data['fecha']
           autor=request.user
           articulo=Articulo(titulo=titulo, subtitulo=subtitulo,cuerpo=cuerpo,fecha=fecha,autor=autor)
           articulo.save()

           
            
        url_exitosa=reverse(crear_articulo)
            
    else:
            formulario=Formulario_Articulo()
            
    http_response=render(
          request=request,
          template_name='AppBlog/crear_articulo.html',
          context={'formulario': formulario}
            
            
        )
        
    return http_response

def buscar_articulo(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        articulos = Articulo.objects.filter(titulo__contains=busqueda)
        contexto = {
            "articulos": articulos,
        }
        http_response = render(
            request=request,
            template_name='AppBlog/lista_articulos.html',
            context=contexto,
        )
        return http_response

    
class ArticuloListView(ListView):
    model = Articulo
    template_name = 'AppBlog/lista_articulos.html'
    context_object_name = 'articulos'
    
    
class ArticuloDetailView(DetailView):
    model = Articulo
    template_name = 'AppBlog/detalle_articulo.html'
    context_object_name = 'articulos'

    success_url = reverse_lazy('detalle_articulo')


class ArticuloUpdateView(LoginRequiredMixin, UpdateView):
    model = Articulo
    template_name = 'AppBlog/detalle_articulo.html'
    fields = ('titulo', 'subtitulo', 'cuerpo')
    success_url = reverse_lazy('editar_articulo')


class ArticuloDeleteView(LoginRequiredMixin, DeleteView):
    model = Articulo
    template_name = 'AppBlog/borrar_articulo.html'

    success_url = reverse_lazy('borrar_articulo')
    
    
@login_required
def editar_articulo(request,id):
    if request.method=="GET": 
        articulo=get_object_or_404(Articulo,id=id)
        formulario=Formulario_Articulo(instance=articulo)
        context={"formulario":formulario}
        return render (
            request,
            "editar_articulo.html" ,
            context
            
        )
        
        
    if request.method=="POST":
        formulario=Formulario_Articulo(request.POST)
        
        if formulario.is_valid(): 
           data = formulario.cleaned_data
           titulo=data['titulo']
           subtitulo=data['subtitulo']
           cuerpo=data['cuerpo']
           fecha=data['fecha']
           autor=request.user
           articulo=Articulo(titulo=titulo, subtitulo=subtitulo,cuerpo=cuerpo,fecha=fecha,autor=autor)
           articulo.save()

           
            
        url_exitosa=reverse(editar_articulo)