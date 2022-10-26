from django import forms
from tracker.models import Project
from django.contrib.auth.models import User

class DatePickerInput(forms.DateInput):
    input_type = 'date'

class ProjectForm(forms.ModelForm):
    started_date = forms.DateField(widget=DatePickerInput(attrs={'class':'form-control'}))
    finished_date = forms.DateField(widget=DatePickerInput(attrs={'class':'form-control'}))
    participants = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.SelectMultiple(attrs={'class':'form-control form-control-custom'}))
    class Meta:
        model = Project
        fields = ('started_date', 'finished_date', 'name', 'description')
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
        }
