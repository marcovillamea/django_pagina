import http

from http.client import HTTPResponse

from django.http import HttpResponse




def saludo(request):
    return HttpResponse("hola este es el segundo intento")

    