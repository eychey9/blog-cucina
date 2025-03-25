from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    
    class Meta:
        verbose_name_plural = "Categorie"
    
    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse('categoria_detail', kwargs={'slug': self.slug})

class Articolo(models.Model):
    titolo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    contenuto = models.TextField()
    immagine = models.ImageField(upload_to='articoli/', blank=True, null=True)
    data_pubblicazione = models.DateTimeField(default=timezone.now)
    autore = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    tempo_preparazione = models.PositiveIntegerField(help_text="Tempo in minuti", default=30)
    difficolta = models.CharField(max_length=20, choices=[
        ('facile', 'Facile'),
        ('media', 'Media'),
        ('difficile', 'Difficile')
    ], default='media')
    
    class Meta:
        ordering = ['-data_pubblicazione']
    
    def __str__(self):
        return self.titolo
    
    def get_absolute_url(self):
        return reverse('articolo_detail', kwargs={'slug': self.slug})

class Commento(models.Model):
    articolo = models.ForeignKey(Articolo, on_delete=models.CASCADE, related_name='commenti')
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    testo = models.TextField()
    data_creazione = models.DateTimeField(auto_now_add=True)
    attivo = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['data_creazione']
    
    def __str__(self):
        return f'Commento di {self.nome} su {self.articolo}'
