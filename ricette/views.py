from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Articolo, Categoria
from .forms import CommentoForm, ArticoloForm
from django.contrib import messages

class HomeView(ListView):
    model = Articolo
    template_name = 'ricette/home.html'
    context_object_name = 'articoli'
    paginate_by = 6
    
    def get_categorie(self):
        return Categoria.objects.all()

class ArticoloDetailView(DetailView):
    model = Articolo
    template_name = 'ricette/articolo_detail.html'
    context_object_name = 'articolo'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articolo = self.get_object()
        commenti = articolo.commenti.filter(attivo=True)
        context['commenti'] = commenti
        context['commento_form'] = CommentoForm()
        return context
    
    def post(self, request, *args, **kwargs):
        articolo = self.get_object()
        form = CommentoForm(request.POST)
        if form.is_valid():
            commento = form.save(commit=False)
            commento.articolo = articolo
            commento.save()
            messages.success(request, 'Il tuo commento è stato aggiunto!')
            return redirect(articolo.get_absolute_url())
        else:
            context = self.get_context_data(**kwargs)
            context['commento_form'] = form
            return render(request, self.template_name, context)

class CategoriaDetailView(ListView):
    template_name = 'ricette/categoria_detail.html'
    context_object_name = 'articoli'
    paginate_by = 6
    
    def get_queryset(self):
        self.categoria = get_object_or_404(Categoria, slug=self.kwargs['slug'])
        return Articolo.objects.filter(categoria=self.categoria)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categoria'] = self.categoria
        return context

class ArticoloCreateView(LoginRequiredMixin, CreateView):
    model = Articolo
    form_class = ArticoloForm
    template_name = 'ricette/articolo_form.html'
    
    def form_valid(self, form):
        form.instance.autore = self.request.user
        messages.success(self.request, 'Articolo creato con successo!')
        return super().form_valid(form)

class ArticoloUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Articolo
    form_class = ArticoloForm
    template_name = 'ricette/articolo_form.html'
    
    def form_valid(self, form):
        form.instance.autore = self.request.user
        messages.success(self.request, 'Articolo aggiornato con successo!')
        return super().form_valid(form)
    
    def test_func(self):
        articolo = self.get_object()
        return self.request.user == articolo.autore

class ArticoloDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Articolo
    template_name = 'ricette/articolo_confirm_delete.html'
    success_url = reverse_lazy('home')
    
    def test_func(self):
        articolo = self.get_object()
        return self.request.user == articolo.autore
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Articolo eliminato con successo!')
        return super().delete(request, *args, **kwargs)

def about(request):
    return render(request, 'ricette/about.html', {'title': 'Chi Siamo'})
