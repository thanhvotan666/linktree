from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.link_create, name='link_create'),
    path('<int:link_id>/edit/', views.link_edit, name='link_edit'),
    path('<int:link_id>/delete/', views.link_delete, name='link_delete'),

    path('l/<int:link_id>/', views.link_click, name='link_click'),
]
