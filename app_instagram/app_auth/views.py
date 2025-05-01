from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm
from django.contrib import messages
from django.views.generic import TemplateView


# Create your views here.
class RegisterView(View):
    template_name = 'app_auth/register.html'
    form_class = RegisterForm

    def dispatch(self, request):
        if request.user.is_authenticated:
            return redirect(to='app_main:home')
        return super().dispatch(request)

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect(to='app_auth:signin')
        return render(request, self.template_name, {'form': form})
