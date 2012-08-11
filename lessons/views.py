from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello! You've reached the lesson interface")

def detail(request, lesson_id):
	return HttpResponse("You're looking at lesson %s." % lesson_id)
