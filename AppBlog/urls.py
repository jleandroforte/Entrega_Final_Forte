

from django.urls import path, include
from AppBlog import views
from .views import ArticuloListView, ArticuloDeleteView,ArticuloUpdateView,ArticuloDetailView


urlpatterns = [
   path('',views.inicio, name='Inicio'),
   path('pages/',ArticuloListView.as_view(), name='Articulos'),  
   path('crear_articulo/', views.crear_articulo, name='crear_articulo'),
   path('buscar_articulo/', views.buscar_articulo, name='buscar_articulo'),
   path('about/',views.about, name='About'), 
   path('pages/<int:pk>/', ArticuloDetailView.as_view(), name="detalle_articulo"),
   path('editar_articulo/<int:pk>/', ArticuloUpdateView.as_view(), name='editar_articulo'),
   path('borrar_articulo/<int:pk>/', ArticuloDeleteView.as_view(), name="borrar_articulo"),
]