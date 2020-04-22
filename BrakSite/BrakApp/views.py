from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'BrakApp/index.html')


def error(request):
    return render(request, '404.html')


def create(request):
    return render(request, 'BrakApp/create.html')
