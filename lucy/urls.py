from django.contrib import admin
from django.urls import path
from lucy.views import index

urlpatterns = [
    path('',index)
]