
from django.shortcuts import render
from django.http import HttpResponse

#home
def home(request):
  return HttpResponse('<h1>Angels Treasures</h1>')
