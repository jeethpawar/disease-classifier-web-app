from django.shortcuts import get_object_or_404, render
from catalog.forms import SymptomForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext

from catalog.util import *
from catalog.forms import SymptomForm
from catalog.diseases import DiseaseInfo

from joblib import dump, load
import pandas as pd
import logging

clf = load('model/mini-model-08-31.joblib')
diseaseInfo = DiseaseInfo()

def index(request):
    if request.method == 'POST':
        form = SymptomForm(request.POST)
        if form.is_valid():
            context = {}

            # 2. Obtain form data
            N_SYMPTOMS = 278
            example = [False]*N_SYMPTOMS # 278 is the number of symptoms we consider (use 321 for the web app)
            example[0] = True
            example_prop = row_prop(example)
            pred = model_predict(clf, [example_prop])
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
                
                symptoms = form.cleaned_data.get('symptoms')
                return render(request, 'results_page.html', context)
            
            else:
                return render(request, 'index.html')
            
            
            
    else:   
        form = SymptomForm()
    return render(request, 'index.html', {'form': form})

def results_page(request):
    return render(request, 'results_page.html')
