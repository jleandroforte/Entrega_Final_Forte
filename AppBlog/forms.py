

from django import forms
from .models import Articulo

class Formulario_Articulo(forms.ModelForm): 
    
    """titulo=forms.CharField(max_length=999) 
    subtitulo=forms.CharField(max_length=999)
    cuerpo=forms.CharField(widget=forms.Textarea) 
    fecha=forms.DateField()
    autor=forms.CharField(max_length=255)"""
    class Meta:
        model = Articulo
        fields = ['titulo','subtitulo','cuerpo','autor']

