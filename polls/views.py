# Create your views here.

from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, world. You are at the freaking poll index.")
