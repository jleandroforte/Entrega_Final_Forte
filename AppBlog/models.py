from django.db import models
from datetime import *
from django.conf import settings

# Create your models here.

class Articulo(models.Model): 
    titulo=models.CharField(max_length=999) 
    subtitulo=models.CharField(max_length=999)
    cuerpo=models.TextField() 
    fecha=models.DateField(null=False, blank=False, auto_now_add=True)
    autor=models.CharField(max_length=255)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.titulo} | {self.subtitulo} | {self.cuerpo} | {self.fecha} | {self.autor}"