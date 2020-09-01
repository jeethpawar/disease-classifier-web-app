from django.shortcuts import get_object_or_404, render
from catalog.forms import SymptomForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
def index(request):
    if request.method == 'POST':
        form = SymptomForm(request.POST)
        if form.is_valid():
            context = {}

            model_results = {}
            model_results['disease_id_0'] = '1'

            context['results'] = model_results
            context['1'] = 'Influenza'
        
            symptoms = form.cleaned_data.get('symptoms') 
            return render(request, 'results_page.html', context)
            
            
    else:   
        form = SymptomForm()
    return render(request, 'index.html', {'form': form})

def results_page(request):
    return render(request, 'results_page.html')
def future_steps(request):
    return render(request, 'future_steps.html')