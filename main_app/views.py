from pyexpat import model
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from main_app.models import Jewelry, Bead
from .forms import CustomerForm

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')

def jewelry_index(request):
  jewelry = Jewelry.objects.all()
  return render(request, 'jewelry/index.html', { 'jewelry': jewelry })