
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('jewelry/', views.jewelry_index, name='index'),
    
    path('jewelry/<int:jewelry_id>/', views.jewelry_detail, name='detail'),
    # new route used to show a form and create jewelry
    
    path('jewelry/create/', views.JewelryCreate.as_view(), name='jewelry_create'),
    path('jewelry/<int:pk>/update', views.JewelryUpdate.as_view(), name='jewelry_update'),
    path('jewelry/<int:pk>/delete', views.JewelryDelete.as_view(), name='jewelry_delete'),

] 