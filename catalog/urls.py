from django.urls import path
from . import views
from .views import results_page, test
from django.contrib.flatpages import views as flat_views
urlpatterns = [
    path('', views.index, name='index'),
    path('results_page', views.results_page, name = 'results_page'),
    path('', views.test, name='test'),
    path('ajax/complete/', views.autocomplete, name='autocomplete')
]