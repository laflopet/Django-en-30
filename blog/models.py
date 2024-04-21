from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=250) # es igual a un varchar en bases de datos
    slug = models.SlugField(max_length=250) # 
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now) #fecha de publicacion actual
    created = models.DateTimeField(auto_now_add=True) #este campo se agrega cada ves que se crea un post
    updated = models.DateTimeField(auto_now=True) #este campo se agrega solo cada vez que se actualiza

    class Meta(): # clases internas (se crean dentro de otra clase) se les llama metaclase
        ordering = ["-publish"] # ordenamiento inverso teniendo en cuenta la columna de publish
        indexes = [
            models.Index(fields=["-publish"]),
        ]

    def __str__(self):
        return self.title
