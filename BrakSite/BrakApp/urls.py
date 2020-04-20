from django.urls import path

from BrakSite.BrakApp.migrations import views

urlpatterns = [
    path('', views.index, name='index')
]