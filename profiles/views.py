from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileStyleForm

# Create your views here.
def profile_view(request, username):
    profile = Profile.objects.select_related('user').get(user__username=username)
    links = profile.user.links.all()

    return render(request, 'profiles/profile.html', {
        'profile': profile,
        'links': links,
    })

@login_required
def profile_style_view(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileStyleForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('public_profile', username=request.user.username)
    else:
        form = ProfileStyleForm(instance=profile)

    return render(request, 'profiles/style.html', {'form': form})
