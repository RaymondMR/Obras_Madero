from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from  .forms  import RegisterForm



# Create your views here.

class SignupView(CreateView):
    form_class=RegisterForm
    template_name='user_management/register.html'
    success_url='/obras'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().get(request, *args, **kwargs)
    
class LoginInterfaceView(LoginView):
    template_name='user_management/login.html'
	
class LogoutInterfaceView(LogoutView):
    template_name='user_management/logout.html'