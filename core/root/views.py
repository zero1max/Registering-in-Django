from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import UserRegisterForm, UserLoginForm 
from services.bot import send_msg

@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
    template_name = 'root/login.html'

class RegisterView(CreateView):
    form_class = UserRegisterForm 
    template_name = 'root/register.html'
    success_url = '/login/' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Register'
        return context
    
    def form_valid(self, form):
        send_msg("Registered New User")
        form.save()

class CustomLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'root/login.html'
    
    def form_valid(self, form):
        user = form.get_user()
        send_msg("Logined New User")
        login(self.request, user)
        return redirect('home')
    
    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password")
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        return context
    
def user_logout(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request, 'root/home.html')