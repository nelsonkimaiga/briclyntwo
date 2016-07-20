from django.shortcuts import render

# Create your views here.


def index(request):
	context = RequestContext
	return render(request, 'official/index.html', context_instance=RequestContext(request))
