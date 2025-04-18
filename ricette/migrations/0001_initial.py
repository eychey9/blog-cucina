# Generated by Django 5.1.7 on 2025-03-25 15:27

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categorie',
            },
        ),
        migrations.CreateModel(
            name='Articolo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('contenuto', models.TextField()),
                ('immagine', models.ImageField(blank=True, null=True, upload_to='articoli/')),
                ('data_pubblicazione', models.DateTimeField(default=django.utils.timezone.now)),
                ('tempo_preparazione', models.PositiveIntegerField(default=30, help_text='Tempo in minuti')),
                ('difficolta', models.CharField(choices=[('facile', 'Facile'), ('media', 'Media'), ('difficile', 'Difficile')], default='media', max_length=20)),
                ('autore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ricette.categoria')),
            ],
            options={
                'ordering': ['-data_pubblicazione'],
            },
        ),
        migrations.CreateModel(
            name='Commento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('testo', models.TextField()),
                ('data_creazione', models.DateTimeField(auto_now_add=True)),
                ('attivo', models.BooleanField(default=True)),
                ('articolo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commenti', to='ricette.articolo')),
            ],
            options={
                'ordering': ['data_creazione'],
            },
        ),
    ]
