from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('404', views.error, name='error'),
    path('create/group', views.create_group, name='create_group'),
    path('create/group/<int:groupID>/member', views.create_groupmember, name='create_groupmember'),
    path('create/group/<int:groupID>/brak', views.create_brak, name='create_brak'),
    path('stats/<int:groupID>', views.stats, name='stats'),
    path('group/<int:groupID>', views.group, name='group'),
]