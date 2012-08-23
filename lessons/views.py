from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404,HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.models import User

import datetime

from django.contrib.auth.decorators import login_required

from lessons.models import Lesson, Promise, Assessment, AssessmentResponse
from lessons.forms import LessonAddForm, PromiseForm, PromiseMakeForm, AssessmentForm, AssessmentAddForm

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
    a = Assessment.objects.get(pk=p.assessment.id)
    form = PromiseForm(initial={'done': 1 if p.done else 0 })
    return render_to_response('lessons/promise_detail.html', {'promise': p, 'form': form, 'assessment': a},
                               context_instance=RequestContext(request))

@login_required
def keep(request, promise_id):
    p = get_object_or_404(Promise, pk=promise_id)
    if request.method == 'POST':
        form = PromiseForm(request.POST)
        if form.is_valid(): # if someone is not being a jerk
            p.done = True if form.cleaned_data['done'] == 1 else False
            print p.done
            if form.cleaned_data['done'] == 1:
                p.save()
                return HttpResponseRedirect(reverse('lessons.views.do_assessment', args=(p.id,)))
            else:
                p.save()
                return HttpResponseRedirect(reverse('lessons.views.promise_detail', args=(p.id,)))
        else: 
            return HttpResponseRedirect(reverse('lessons.views.promise_detail', args=(p.id,)))
    else:
        form = PromiseForm({'done': 1 if p.done else 0 })
        return render_to_response('lessons/promise_detail.html', {
            'promise': p,
            'form': form,
            }, context_instance=RequestContext(request))

@login_required
def lesson_add(request):
    # This is how you do it with a functional view <side eye>
    if request.method == 'POST':
        form = LessonAddForm(request.POST)
        if form.is_valid():
            l = Lesson()
            l.name = form.cleaned_data['name']
            l.url = form.cleaned_data['url']
            l.save()
            return HttpResponseRedirect(reverse('lessons.views.detail', args=(l.id,)))
        else:
            # will return errors if any, and prepopulate what was passed in before
            return render_to_response('lessons/add.html', { 'form': form }, context_instance=RequestContext(request))
    else: 
        form = LessonAddForm()  
        return render_to_response('lessons/add.html', { 'form': form }, context_instance=RequestContext(request))

@login_required
def promise_add(request):
    # This is how you do it with a functional view <side eye>
    if request.method == 'POST':
        form = PromiseMakeForm(request.POST)
        if form.is_valid():
            p = Promise()
            p.who = form.cleaned_data['who']
            # hopefully this happens magically
            p.made_by = User.objects.get(pk=request.user.id)
            p.when = form.cleaned_data['when']
            p.lesson = Lesson.objects.get(pk=form.cleaned_data['lesson'])
            p.assessment = Assessment.objects.get(pk=form.cleaned_data['assessment'])
            p.save()
            return HttpResponseRedirect(reverse('lessons.views.promise_detail', args=(p.id,)))
        else:
            # will return errors if any, and prepopulate what was passed in before
            made_by = request.user.id
            return render_to_response('lessons/promise_add.html', { 'form': form, 'made_by': made_by }, context_instance=RequestContext(request))
    else: 
        form = PromiseMakeForm()    
        made_by = request.user.id
        return render_to_response('lessons/promise_add.html', { 'form': form, 'made_by': made_by }, context_instance=RequestContext(request))

@login_required
def do_assessment(request, promise_id):
    """
    Taking care of an assessment for a promise kept
    """
    if request.method == 'POST':
        form = AssessmentForm(request.POST)
        if form.is_valid():
            ar = AssessmentResponse()
            ar.promise = Promise.objects.get(pk=promise_id)
            ar.post = form.cleaned_data['post']
            ar.save()
            return HttpResponseRedirect(reverse('lessons.views.promise_detail', args=(promise_id,)))
    else: 
        p = get_object_or_404(Promise, pk=promise_id)
        a = get_object_or_404(Assessment, pk=p.assessment.id)
        form = AssessmentForm()
        if p.done == True:
            return render_to_response('assessments/detail.html', {
                'promise': p,
                'assessment': a,
                'form': form,
            }, context_instance=RequestContext(request))
        else:
            # this is actually an error at this point...
            return render_to_response('lessons/promise_detail.html', {'promise': p},
                                       context_instance=RequestContext(request))

@login_required
def add_assessment(request):
    if request.method == 'POST':
        form = AssessmentAddForm(request.POST)
        if form.is_valid(): 
            assess = Assessment()
            assess.question = form.cleaned_data['question']
            print assess
            assess.save()
            return HttpResponseRedirect(reverse('lessons.views.assessments'))
        else:
            return render_to_response('assessments/add.html', { 'form': form }, context_instance=RequestContext(request))
    else:
        form = AssessmentAddForm()
        return render_to_response('assessments/add.html', { 'form': form }, context_instance=RequestContext(request))

def assessments(request):
    assessments = Assessment.objects.all()
    return render_to_response('assessments/all.html', { 'assessments': assessments }, context_instance=RequestContext(request))

def front_page(request):
    form = PromiseMakeForm()    
    made_by = request.user.id if request.user.id else 'Bogus'
    return render_to_response('lessons/promise_add.html', { 'form': form, 'made_by': made_by }, context_instance=RequestContext(request))
