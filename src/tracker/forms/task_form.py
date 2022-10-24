from django import forms
from tracker.models import Task
from tracker.models import Type



class TaskForm(forms.ModelForm):
    types=forms.ModelMultipleChoiceField(queryset=Type.objects.all(), widget=forms.SelectMultiple(attrs={'class':'form-control'}))
    class Meta:
        model = Task
        fields = ('summary', 'description', 'status', 'types')
        widgets = {
            'summary':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
        }