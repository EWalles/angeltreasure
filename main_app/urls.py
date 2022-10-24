
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('jewelry/', views.jewelry_index, name='index'),
    
    path('jewelry/<int:cat_id>/', views.jewelry_detail, name='detail'),
    # new route used to show a form and create jewelry
    
    path('jewelry/create/', views.JewelryCreate.as_view(), name='jewelry_create'),
    path('jewelry/<int:pk>/update', views.JewelryUpdate.as_view(), name='jewelry_update'),
    path('jewelry/<int:pk>/delete', views.JewelryDelete.as_view(), name='jewelry_delete'),
    path('beads/', views.BeadList.as_view(), name='beads_index'),
    path('beads/<int:pk>/', views.BeadDetail.as_view(), name='beads_detail'),
    path('beads/create/', views.BeadCreate.as_view(), name='beads_create'),
    path('beads/<int:pk>/update/', views.BeadUpdate.as_view(), name='beads_update'),
    path('beads/<int:pk>/delete/', views.BeadDelete.as_view(), name='beads_delete'),
    path('jewelry/<int:jewelry_id>/assoc_bead/<int:bead_id>/', views.assoc_bead, name='assoc_bead'),
] 