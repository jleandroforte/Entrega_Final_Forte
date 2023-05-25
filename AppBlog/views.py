
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

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, View

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
           autor=request.user
           owner=request.user
           articulo=Articulo(titulo=titulo, subtitulo=subtitulo,cuerpo=cuerpo,autor=autor,owner=owner)
           articulo.save()

           
            
        url_exitosa=reverse(crear_articulo)
            
    else:
            formulario=Formulario_Articulo()
            
    http_response=render(
        request=request,
        template_name='AppBlog/crear_articulo.html',
        context={'formulario': formulario})
        
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


class ArticuloUpdateView(LoginRequiredMixin, View):
    model = Articulo
    template_name = 'AppBlog/detalle_articulo.html'
    fields = ['titulo', 'subtitulo', 'cuerpo','autor']
    fields_exclude = ['fecha']
    success_url = reverse_lazy('Articulos')
    
    def get(self, request, pk):
        art = get_object_or_404(Articulo, id=pk)
        form = Formulario_Articulo(instance=art)
        ctx = {'formulario': form,'articulo':art}
        return render(request, 'AppBlog/editar_articulo.html', ctx)
    
    def post(self, request, pk=None):
        art = get_object_or_404(Articulo, id=pk)
        form = Formulario_Articulo(request.POST, instance=art)

        if not form.is_valid():
            ctx = {'formulario': form}
            return render(request, self.template_name, ctx)

        form.save()
        return redirect(self.success_url)


class ArticuloDeleteView(LoginRequiredMixin, DeleteView):
    model = Articulo
    template_name = 'AppBlog/borrar_articulo.html'
    success_url = reverse_lazy('borrar_articulo')
    