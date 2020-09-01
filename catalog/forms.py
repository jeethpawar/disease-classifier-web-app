from django import forms
from django.forms import MultipleChoiceField
from django.forms import CheckboxSelectMultiple


class SymptomForm(forms.Form):
    OPTIONS = (
        ["symp1", "Cough"],
        ["symp2", 'Bodyache'],
        ['symp3', 'Fever'],
    )
    Symptoms = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple, choices = OPTIONS)