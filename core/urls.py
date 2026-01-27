from django.urls import path
from .views import landing_page, public_profile

urlpatterns = [
    path('', landing_page, name='landing'),
    path('<str:username>/', public_profile, name='public_profile'),
]
