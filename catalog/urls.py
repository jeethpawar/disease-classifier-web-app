from django.urls import path
from . import views
from .views import results_page
from django.contrib.flatpages import views as flat_views
urlpatterns = [
    path('', views.index, name='index'),
    path('results_page', views.results_page, name = 'results_page'),
    path('ajax/complete/', views.check_symptom_checkbox, name='check_checkbox'),
    path('ajax/complete/1', views.autocomplete_search, name='autocomplete_search')
]