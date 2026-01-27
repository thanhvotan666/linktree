from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

def landing_page(request):
    return render(request, 'core/landing.html')

def public_profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = user.profile

    links = profile.links.filter(is_active=True)

    return render(request, 'public/profile.html', {
        'profile': profile,
        'links': links
    })
