from django import forms
from .models import Commento, Articolo

class CommentoForm(forms.ModelForm):
    class Meta:
        model = Commento
        fields = ('nome', 'email', 'testo')
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'testo': forms.Textarea(attrs={'class': 'form-control'}),
        }

class ArticoloForm(forms.ModelForm):
    class Meta:
        model = Articolo
        fields = ('titolo', 'slug', 'contenuto', 'immagine', 'categoria', 'tempo_preparazione', 'difficolta')
        widgets = {
            'titolo': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'contenuto': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'tempo_preparazione': forms.NumberInput(attrs={'class': 'form-control'}),
            'difficolta': forms.Select(attrs={'class': 'form-control'}),
        }