from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=50, label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(required=True, label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))




class CustomeUserCreationForm(forms.ModelForm):
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Повторите пароль'}))
    class Meta:
        model = User
        fields = ('username', 'password_confirm', 'password','first_name', 'last_name', 'email')
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Введите ваш логин'}),
            'password':forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Введите пароль'}),
            'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Введите ваше имя'}),
            'last_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Введите фамилию'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Введите почтовый ящик'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise ValidationError('Пароли не совпадают')
        
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user



