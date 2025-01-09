from django.shortcuts import redirect, render
from .forms import UserRegisterForm, UserLoginForm 
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib import messages


class RegisterView(CreateView):
    form_class = UserRegisterForm 
    template_name = 'root/register.html'
    success_url = '/login/' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Register'
        return context
    

class CustomLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'root/login.html'
    
    def form_valid(self, form):
        user = form.get_user()
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