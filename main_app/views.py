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
  return render(request, 'jewelry/index.html', { 'Jewelry': Jewelry })

def jewelry_detail(request, jewelry_id):
  jewelry = Jewelry.objects.get(id=jewelry_id)
  beads_jewelry_doesnt_have = Bead.objects.exclude(id__in = Jewelry.beads.all().values_list('id'))
  return render(request, 'jewelry/detail.html')

def assoc_bead(request, jewelry_id, bead_id):
  # Note that you can pass a toy's id instead of the whole object
   Jewelry.objects.get(id=jewelry_id).bead.add(bead_id)
   return redirect('detail', jewelry_id=jewelry_id)

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

class BeadCreate(CreateView):
    model = Bead
    fields = ('name', 'color')

class BeadUpdate(UpdateView):
    model = Bead
    fields = ('name', 'color')

class BeadDelete(DeleteView):
    model = Bead
    success_url = '/toys/'

class BeadDetail(DetailView):
    model = Bead
    template_name = 'beads/detail.html'

class BeadList(ListView):
    model = Bead
    template_name = 'beads/index.html'
    
