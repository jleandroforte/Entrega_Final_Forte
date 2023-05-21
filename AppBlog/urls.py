

from django.urls import path, include
from AppBlog import views
from .views import ArticuloListView


urlpatterns = [
   path('',views.inicio, name='Inicio'),
   path('pages/',ArticuloListView.as_view(), name='Articulos'),  
   path('crear_articulo/', views.crear_articulo, name='crear_articulo'),
   path('buscar_articulo/', views.buscar_articulo, name='buscar_articulo'),

   
   path('about/',views.about, name='About'), 
  
   

]