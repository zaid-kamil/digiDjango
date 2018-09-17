from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import JsonResponse
from .models import TaskRequest
from .forms import TaskRequestForm

# Create your views here.

class SignUp(generic.CreateView):
    form_class =  UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html' 

class HomeView(generic.ListView):
    model = TaskRequest
    form_class = TaskRequestForm
    success_url = reverse_lazy('home')
    template_name = "index.html"
    context_object_name = "task_list"

class SearchView(generic.TemplateView):
    template_name = "searchpage.html"

