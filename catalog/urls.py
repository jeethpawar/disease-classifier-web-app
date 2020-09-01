from django.urls import path
from . import views
from .views import results_page, future_steps
from django.contrib.flatpages import views as flat_views
urlpatterns = [
    path('', views.index, name='index'),
    path('results_page', views.results_page, name = 'results_page'),
    path('future_steps', views.future_steps, name = 'future_steps'),
]
