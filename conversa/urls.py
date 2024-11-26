from django.urls import path
from conversa.views import index, imagem

urlpatterns = [
    path('', index, name='index'),
]