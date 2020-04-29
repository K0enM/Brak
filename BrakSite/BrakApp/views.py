from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import GroupForm
from .models import Group, Groupmember


# TODO Manier bedenken voor dynamic content of house pagina of losse overzichts pagina;

# Create your views here.
def index(request):
    return render(request, 'BrakApp/index.html')


def error(request):
    return render(request, '404.html')


def create(request):
    form = GroupForm(request.POST or None)
    if form.is_valid():
        group = form.save()
        pk = group.pk
        messages.success(request, pk)
        return HttpResponseRedirect(request.path)
    context = {
        'form': form
    }
    return render(request, 'BrakApp/create.html', context)


def house(request, groupID):
    groupObj = get_object_or_404(Group, pk=groupID)
    try:
        groupMembers = Groupmember.objects.filter(Group=groupObj)
        context = {
            'group': groupObj,
            'groupMembers': groupMembers
        }
    except ObjectDoesNotExist:
        context = {
            'group': groupObj
        }

    return render(request, 'BrakApp/house.html', context)
