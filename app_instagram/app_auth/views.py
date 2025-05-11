from django.views import View
from .forms import RegisterForm

from django.contrib import messages

from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


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


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'app_auth/password_reset.html'  # Заміни на правильний шаблон
    email_template_name = 'app_auth/password_reset_email.html'  # І цей також
    html_email_template_name = 'app_auth/password_reset_email.html'  # І цей
    success_url = reverse_lazy('app_auth:password_reset_done')  # Переконайся, що цей URL правильний
    success_message = "An email with instructions to reset your password has been sent to %(email)s."
    subject_template_name = 'app_auth/password_reset_subject.txt'  # І цей шаблон
