from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
                        .filter(status=Post.Status.PUBLISHED)

class Post(models.Model):


    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250) # es igual a un varchar en bases de datos
    slug = models.SlugField(max_length=250, unique_for_date='publish') 
    author = models.ForeignKey(User,   # relacion muchos a 1.  un post solo puede pertenecer a un usuario.
                               on_delete=models.CASCADE, # se eliminan en cascada usuarios con post
                               related_name='blog_posts') # verificar desde la clase de usuarios cuantos post a hecho.

    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now) #fecha de publicacion actual
    created = models.DateTimeField(auto_now_add=True) #este campo se agrega cada ves que se crea un post
    updated = models.DateTimeField(auto_now=True) #este campo se agrega solo cada vez que se actualiza
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    objects = models.Manager()
    published = PublishedManager()

    class Meta: # clases internas (se crean dentro de otra clase) se les llama metaclase
        ordering = ["-publish"] # ordenamiento inverso teniendo en cuenta la columna de publish
        indexes = [
            models.Index(fields=["-publish"]),
        ]

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year,
                                                 self.publish.month,
                                                 self.publish.day,
                                                 self.slug,
                                                 ])
    

class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]


    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
    
    