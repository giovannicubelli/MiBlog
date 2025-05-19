from django.db import models

from django.utils import timezone

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="posts")
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name="posts")
    # imagen = models.ImageField(upload_to='posts_images/', blank=True, null=True) # Opcional

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-fecha_publicacion']
