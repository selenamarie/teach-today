from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404,HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext

from django.contrib.auth.decorators import login_required

from lessons.models import Lesson, Promise
from lessons.forms import LessonAddForm, PromiseForm, PromiseMakeForm

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
    form = PromiseForm(initial={'done': 1 if p.done else 0 })
    return render_to_response('lessons/promise_detail.html', {'promise': p, 'form': form},
                               context_instance=RequestContext(request))

@login_required
def keep(request, promise_id):
    p = get_object_or_404(Promise, pk=promise_id)
    if request.method == 'POST':
        form = PromiseForm(request.POST)
        if form.is_valid(): # if someone is not being a jerk
            p.done = True if form.cleaned_data['done'] == 1 else False
            print p.done
            if p.done:
                p.save()
                return HttpResponseRedirect(reverse('lessons.views.keep_promise', args=(p.id,)))
            else:
                p.save()
                return render_to_response('lessons/promise_detail.html', {
                    'promise': p,
                    'form': form,
                    }, context_instance=RequestContext(request))
        else: 
            return render_to_response('lessons/promise_detail.html', {
                'promise': p,
                'form': form,
                }, context_instance=RequestContext(request))
    else:
        form = PromiseForm({'done': p.done})
        return render_to_response('lessons/promise_detail.html', {
            'promise': p,
            'form': form,
            }, context_instance=RequestContext(request))

@login_required
def keep_promise(request, promise_id):
    # now you need to do a post assessment
    p = get_object_or_404(Promise, pk=promise_id)
    if p.done == True:
        return render_to_response('assessments/detail.html', {
            'promise': p,
        }, context_instance=RequestContext(request))
    else:
        return render_to_response('lessons/promise_detail.html', {'promise': p},
                                   context_instance=RequestContext(request))

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
            p.lesson = Lesson.objects.get(pk=form.cleaned_data['lesson'])
            p.when = form.cleaned_data['when']
            p.save()
            return HttpResponseRedirect(reverse('lessons.views.promise_detail', args=(p.id,)))
        else:
            # will return errors if any, and prepopulate what was passed in before
            return render_to_response('lessons/promise_add.html', { 'form': form }, context_instance=RequestContext(request))
    else: 
        form = PromiseMakeForm()    
        made_by = request.user.id
        return render_to_response('lessons/promise_add.html', { 'form': form, 'made_by': made_by }, context_instance=RequestContext(request))



