from django.shortcuts import get_object_or_404, render
from catalog.forms import SymptomForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.http import JsonResponse

from catalog.util import *
from catalog.forms import SymptomForm
from catalog.diseases import DiseaseInfo
from catalog.autocomplete import *
from joblib import dump, load
import pandas as pd
import logging

clf = load('model/mini-model-08-31.joblib')
#clf = load('model/fullmodel.joblib')
diseaseInfo = DiseaseInfo()
autocomplete = AutocompleteSystem()
def index(request):
    if request.method == 'POST':
        form = SymptomForm(request.POST)
        
        if form.is_valid():
            context = {}
            
            # 2. Obtain form data
            #
            form_prop = row_prop(form.as_model_input())
            pred = model_predict(clf, [form_prop])
            results = {}
            if pred: 
                pred_id = int(pred[0])
                pred_0 = {}
                logging.debug('Prediction id = %s' % (pred_id))
                
                name, link = diseaseInfo.get_diseaseinfo(pred_id)
                pred_0['disease_name'] = name
                pred_0['disease_link'] = link

                results['pred_0'] = pred_0
                context['results'] = results
                logging.debug(form.cleaned_data)
                return render(request, 'results_page.html', context)
            
            else:
                return render(request, 'index.html')
            
            
            
    else:   
        form = SymptomForm()
    return render(request, 'index.html', {'form': form})

def results_page(request):
    return render(request, 'results_page.html')


def test(request):
    logging.debug('request: {}'.format(request))
    logging.debug(SymptomForm())
    return render(request, 'index.html')


def autocomplete(request):
    if request.is_ajax():
        logging.debug('cur-search: {}'.format(request.GET.get('search', None)))
        
        # TODO: call autocompleteSystem's search(), and return its output as 
        #       value for 'list' key in data dictionary
        list = ['apple', 'ape', 'ant']
        data = {
            'list' : list
        }
        return JsonResponse(data)
