

from django import forms

class Formulario_Articulo(forms.Form): 
    
    titulo=forms.CharField(max_length=999) 
    subtitulo=forms.CharField(max_length=999)
    cuerpo=forms.CharField(widget=forms.Textarea) 
    fecha=forms.DateField()
    autor=forms.CharField(max_length=255)
    
    
