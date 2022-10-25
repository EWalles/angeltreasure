from pyexpat import model
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from main_app.models import Jewelry, Bead


def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')

def jewelry_index(request):
  jewelry = Jewelry.objects.all()
  return render(request, 'jewelry/index.html', { 'jewelry': jewelry })

def jewelry_detail(request, jewelry_id):
  jewelry = Jewelry.objects.get(id=jewelry_id)
  beads_jewelry_doesnt_have = Bead.objects.exclude(id__in = Jewelry.beads.all().values_list('id'))
  return render(request, 'jewelry/detail.html')



class JewelryCreate(CreateView):
  model = Jewelry
  fields = '__all__'

class JewelryUpdate(UpdateView):
  model = Jewelry
  # Let's disallow the renaming of the cat
  fields = ['name', 'description', 'function']

class JewelryDelete(DeleteView):
  model = Jewelry
  success_url = '/jewelry'


