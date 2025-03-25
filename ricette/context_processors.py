from .models import Categoria

def categorie(request):
    return {'categorie_list': Categoria.objects.all()}