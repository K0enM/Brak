from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('404', views.error, name='error'),
    path('create', views.create, name='create'),
    path('house/<int:groupID>', views.house, name='house')
]