from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Найти задачу'}))
