from django.urls import path
from . import views
from django.contrib.flatpages import views as flat_views
urlpatterns = [
    path('', views.index, name='index'),
]