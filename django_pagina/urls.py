from django.contrib import admin
from django.urls import path

from django_pagina.views import saludo,template



urlpatterns = [
    path('admin/', admin.site.urls),
    path("saludo/",saludo ,name="el saludo"),
    path("template/",template, name="template prueba")
    

]
