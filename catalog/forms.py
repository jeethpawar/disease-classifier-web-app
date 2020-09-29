from django import forms
from django.forms import MultipleChoiceField
from django.forms import CheckboxSelectMultiple
import pandas as pd



def load_options():
    df2 = pd.read_csv('data/symptom_ids.csv')
    res = []

    for i in range(len(df2.columns)):
        if i > 0:
            key = str(i)
            symptom_id = str(i-1)
            res.append([symptom_id, df2[key][0]])
    return tuple(res)

OPTIONS = load_options()

class SymptomForm(forms.Form):
    #OPTIONS = load_options()
    Symptoms = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple, choices = OPTIONS)

    def as_model_input(self):
        symptoms = self.cleaned_data['Symptoms']
        #symptom_form_results = [False]*len(OPTIONS)
        symptom_form_results = [False]*(278)
        for symptom_id in symptoms:
            symptom_form_results[int(symptom_id)] = True
        return symptom_form_results


