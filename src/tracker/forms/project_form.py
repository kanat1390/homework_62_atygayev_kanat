from django import forms
from tracker.models import Project

class DatePickerInput(forms.DateInput):
    input_type = 'date'

class ProjectForm(forms.ModelForm):
    started_date = forms.DateField(widget=DatePickerInput(attrs={'class':'form-control'}))
    finished_date = forms.DateField(widget=DatePickerInput(attrs={'class':'form-control'}))
    class Meta:
        model = Project
        fields = ('started_date', 'finished_date', 'name', 'description')
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
        }
