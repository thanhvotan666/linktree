from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from .models import Link
from .forms import LinkForm

@login_required
def dashboard(request):
    profile = request.user.profile
    links = profile.links.all()

    return render(request, 'dashboard/dashboard.html', {
        'links': links
    })

@login_required
def link_create(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            link = form.save(commit=False)
            link.profile = profile
            link.save()
            return redirect('dashboard')
    else:
        form = LinkForm()

    return render(request, 'dashboard/link_form.html', {
        'form': form
    })

@login_required
def link_edit(request, link_id):
    profile = request.user.profile
    link = get_object_or_404(Link, id=link_id)

    if link.profile != profile:
        return HttpResponseForbidden()

    if request.method == 'POST':
        form = LinkForm(request.POST, instance=link)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = LinkForm(instance=link)

    return render(request, 'dashboard/link_form.html', {
        'form': form
    })

@login_required
def link_delete(request, link_id):
    profile = request.user.profile
    link = get_object_or_404(Link, id=link_id)

    if link.profile != profile:
        return HttpResponseForbidden()

    link.delete()
    return redirect('dashboard')

def link_click(request, link_id):
    link = get_object_or_404(Link, id=link_id, is_active=True)

    link.click_count += 1
    link.save(update_fields=['click_count'])

    return redirect(link.url)
