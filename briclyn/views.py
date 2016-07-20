from django.shortcuts import render
from django.template import RequestContext

from .models import *
from briclyn.forms import *



def index(request):
	return render(request, 'official/index.html', {})
