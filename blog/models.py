from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    color = models.CharField(max_length=60)

    
    def __str__(self):
        return self.nombre

class Book(models.Model):
    BOOK_CHOICES = (
        ('El Capital','El Capital'),
        ('Rebelion en la granja','Rebelion en la granja'),
        ('Big Sur','Big Sur'),
        ('Factotum','Factotum'),
        ('Espera a la primavera, Bandini','Espera a la primavera, Bandini'),
        ('History of France','History of France'),
        ('PHP manual','PHP manual'),
        ('La vida en rojo','La vida en rojo'),
    )
    titulo = models.CharField(max_length = 100, choices = BOOK_CHOICES)

    def __str__(self):
        return self.titulo               