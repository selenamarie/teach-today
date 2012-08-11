from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404

from lessons.models import Lesson, Promise

from django.http import HttpResponse

def index(request):
	latest_lessons = Lesson.objects.all().order_by('-pub_date')[:5]
	return render_to_response('lessons/index.html', {'latest_lessons': latest_lessons})

def detail(request, lesson_id):
	l = get_object_or_404(Lesson, pk=lesson_id)
	return render_to_response('lessons/detail.html', {'lesson': l})

def promises(request):
	latest_promises = Promise.objects.all()
	return render_to_response('lessons/promises.html', {'latest_promises': latest_promises})

