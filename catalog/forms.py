from django import forms
from django.forms import MultipleChoiceField
from django.forms import CheckboxSelectMultiple


class SymptomForm(forms.Form):
    OPTIONS = (
        ['0', "Cough"],
        ['1', 'Bodyache'],
        ['2', 'Fever'],
    )
    Symptoms = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple, choices = OPTIONS)

    def as_model_input(self):
        symptoms = self.cleaned_data['Symptoms']
        results = [False]*278
        for symptom_id in symptoms:
            results[int(symptom_id)] = True
        return results
