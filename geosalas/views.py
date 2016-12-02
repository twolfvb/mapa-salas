from django.shortcuts import render


def mapa(request):
    return render(request, 'index.html')
