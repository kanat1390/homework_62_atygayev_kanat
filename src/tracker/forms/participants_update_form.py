from dataclasses import fields
from tracker.models import Project
from django import forms
from django.contrib.auth.models import User

class ParticipantUpdateForm(forms.ModelForm):
    participants = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.SelectMultiple(attrs={'class':'form-control form-control-custom'}))
    class Meta:
        model = Project
        fields = ('participants',)
