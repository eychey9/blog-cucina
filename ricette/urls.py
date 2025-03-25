from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('articolo/<slug:slug>/', views.ArticoloDetailView.as_view(), name='articolo_detail'),
    path('categoria/<slug:slug>/', views.CategoriaDetailView.as_view(), name='categoria_detail'),
    path('articolo/new/', views.ArticoloCreateView.as_view(), name='articolo_create'),
    path('articolo/<slug:slug>/update/', views.ArticoloUpdateView.as_view(), name='articolo_update'),
    path('articolo/<slug:slug>/delete/', views.ArticoloDeleteView.as_view(), name='articolo_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)