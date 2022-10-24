from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=50, label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(required=True, label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
