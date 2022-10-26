from accounts.forms import LoginForm, CustomeUserCreationForm
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.urls import reverse

class SuccessListUrlMixin:
    def get_success_url(self):
        return redirect(reverse(self.success_url, kwargs={}))

class LoginView(TemplateView):
    template_name = 'accounts/login.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form()
        context = {
            'form': form
        }
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        next = request.GET.get('next', None)
        form = self.form(request.POST)
        if not form.is_valid():
            return redirect('login')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if not user:
            return redirect('login')
        login(request, user)
        return redirect(next) if next else redirect('project-list')


def logout_view(request):
    logout(request)
    return redirect('project-list')


class RegisterView(SuccessListUrlMixin, CreateView):
    template_name = 'accounts/register.html'
    form_class = CustomeUserCreationForm
    success_url = 'project-list'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return self.get_success_url()
        context = {
            'form':form,
        }
        return self.render_to_response(context)




