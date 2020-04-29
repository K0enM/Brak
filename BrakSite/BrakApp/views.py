from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import HuisForm
from .models import Huis, Huisgenoot


# TODO Manier bedenken voor dynamic content of house pagina of losse overzichts pagina;

# Create your views here.
def index(request):
    return render(request, 'BrakApp/index.html')


def error(request):
    return render(request, '404.html')


def create(request):
    form = HuisForm(request.POST or None)
    if form.is_valid():
        huis = form.save()
        pk = huis.pk
        messages.success(request, pk)
        return HttpResponseRedirect(request.path)
    context = {
        'form': form
    }
    return render(request, 'BrakApp/create.html', context)


def house(request, huisID):
    houseObj = get_object_or_404(Huis, pk=huisID)
    try:
        houseMates = Huisgenoot.objects.filter(Huis=houseObj)
        context = {
            'house': houseObj,
            'houseMates': houseMates
        }
    except ObjectDoesNotExist:
        context = {
            'house': houseObj
        }

    return render(request, 'BrakApp/house.html', context)
