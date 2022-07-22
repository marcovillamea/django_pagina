import http

from http.client import HTTPResponse

from django.http import HttpResponse

from django.shortcuts import render


def saludo(request):
    return HttpResponse("hola este es el segundo intento")


def template(request):
    return render(request, "templates.html",context={})

    