from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required


from teach.models import UserProfile
from lessons.models import Promise

def main_page(request):
    return render_to_response('index.html')

def logout_page(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def profile(request):
    """
    Show a user profile
    """
    up = UserProfile.objects.get(user=request.user)
    promises = Promise.objects.filter(made_by=request.user.id)
    return render_to_response('profiles/profile_detail.html', {'profile': up, 'promises': promises})
    return HttpResponseRedirect('/')

@login_required
def profile_individual(request, user):
    """
    Show a user profile
    """
    up = UserProfile.objects.get(user=user)
    promises = Promise.objects.filter(made_by=user)
    return render_to_response('profiles/profile_detail.html', {'profile': up, 'promises': promises})
    return HttpResponseRedirect('/')
