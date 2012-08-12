from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404,HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext

from django.contrib.auth.decorators import login_required

from lessons.models import Lesson, Promise

from django.http import HttpResponse

def index(request):
	latest_lessons = Lesson.objects.all().order_by('-pub_date')[:5]
	return render_to_response('lessons/index.html', {'latest_lessons': latest_lessons})

@login_required
def detail(request, lesson_id):
	l = get_object_or_404(Lesson, pk=lesson_id)
	return render_to_response('lessons/detail.html', {'lesson': l})

@login_required
def promises(request):
	latest_promises = Promise.objects.all()
	return render_to_response('lessons/promises.html', {'latest_promises': latest_promises})

@login_required
def promise_detail(request, promise_id):
	p = get_object_or_404(Promise, pk=promise_id)
	return render_to_response('lessons/promise_detail.html', {'promise': p},
                               context_instance=RequestContext(request))

@login_required
def keep(request, promise_id):
	p = get_object_or_404(Promise, pk=promise_id)
	try:
		if request.POST['done'] == 'False': 
			p.done = False
		else:
			p.done = True
		p.save()
	except (KeyError, Promise.DoesNotExist):
		# Redisplay form
		return render_to_response('promises/detail.html', {
			'promise': p,
			'error_message': "You didn't keep a promise!",
		}, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect(reverse('lessons.views.keep_promise', args=(p.id,)))

@login_required
def keep_promise(request, promise_id):
	p = get_object_or_404(Promise, pk=promise_id)
	return render_to_response('lessons/promise_detail.html', {'promise': p},
                               context_instance=RequestContext(request))

