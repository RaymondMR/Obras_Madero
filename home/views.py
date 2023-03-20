from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect


class HomeView(TemplateView):
    template_name="home/welcome.html"
    extra_context={'today': datetime.today()}

class AuthorizedView(LoginRequiredMixin,TemplateView):
    template_name="home/authorized.html"
    login_url='/admin'

class SignupView(CreateView):
    form_class=UserCreationForm
    template_name='home/register.html'
    success_url='/obras'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().get(request, *args, **kwargs)
	



