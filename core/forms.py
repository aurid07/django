from django import forms
from .models import StepCount

class StepCountForm(forms.ModelForm):
    current_status_choices = [
        ('Completed', 'Completed'),
        ('Running', 'Running'),
        ('Failed', 'Failed'),
    ]
    
    step_count = forms.IntegerField(label='Step Count')
    current_status = forms.ChoiceField(choices=current_status_choices, label='Status')
    
    class Meta:
        model = StepCount
        fields = ['step_count', 'current_status']