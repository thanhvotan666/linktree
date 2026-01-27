# profiles/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('',views.profile_view,name='profile'),
    path('style/', views.profile_style_view, name='profile_style'),

]
