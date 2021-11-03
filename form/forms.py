from django import forms
from .models import Anamnese, Tooth


class AnamneseForm(forms.ModelForm):
    
    class Meta:
        model = Anamnese
        fields = ['pregnant', 'bleeding', 'pressure', 'allergy', 'systemic_disease', 'medicine']

class ToothForm(forms.ModelForm):
    
    class Meta:
        model = Tooth
        fields = ['number', 'report']