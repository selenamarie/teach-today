from django.contrib.auth import logout
from django.http import Http404,HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.models import User

from teach.models import UserProfile
from lessons.models import Promise
from teach.forms import UserProfileForm

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
    try: 
        up = UserProfile.objects.get(user=request.user)
        promises = Promise.objects.filter(made_by=request.user.id)
        return render_to_response('profiles/profile_detail.html', {'profile': up, 'promises': promises})
    except: 
        return HttpResponseRedirect(reverse('teach.views.profile_create', args=(request.user.id,)))

@login_required
def profile_individual(request, user):
    """
    Show a user profile
    """
    up = UserProfile.objects.get(user=user)
    promises = Promise.objects.filter(made_by=user)
    return render_to_response('profiles/profile_detail.html', {'profile': up, 'promises': promises})

@login_required
def profile_create(request, user_id):
    # TODO: verify that user_id == logged in userid
    if request.method == 'POST':
        form = UserProfileForm(requet.POST)
        if form.is_valid():
            up = UserProfile()
            up.user = User.objects.get(pk=form.cleaned_data['user_id'])
            up.favorite_animal = form.cleaned_data['favorite_animal']
            up.save()
            return HttpResponseRedirect(reverse('teach.views.profile_individual', args=(form.cleaned_data['user_id'],)))
        else:
            # will return errors if any -- TODO :D
            return render_to_response('profiles/create_detail.html', {'profile': up, 'promises': promises})
    else:
        up = UserProfile()
        form = UserProfileForm()
        return render_to_response('profiles/create_detail.html', {'profile': up, 'promises': promises})

