from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render,render_to_response, get_object_or_404
from django.utils import timezone
from django.template import RequestContext
from django.contrib.auth import logout
from django.contrib import messages
from .models import *

from urllib import quote_plus


from briclyn.forms import *
from business import request_new_listing
from business import save_customer_listing
from business import send_listing_email


def index(request):
	return render(request, 'official/index.html', {})

def home(request):
	return render(request, 'official/home.html', {})


def edit_profile(request):

	# user = request.user
	user = request.user
	# profile = UserProfile.objects.get(user=user)
	profile = request.user.profile
	user_form = UserForm(request.POST, instance=user)
	profile_form = ProfileForm(request.POST, instance=profile)

	if request.method == 'POST':
		user_form = UserForm(request.POST, instance=user)
		profile_form = ProfileForm(request.POST, instance=profile)

		if user_form.is_valid():
			if profile_form.is_valid():
				user = user_form.save(commit=False)
				profile = profile_form.save(commit=False)
				user.save()
				profile.save()
				messages.success(request, "Successfully Saved Changes!")
				return HttpResponseRedirect('/home')
			else:
				form.ValidationError("Invalid details provided")
		else:
			return form.ValidationError("Invalid details provided")
	else:
		user_form = UserForm(request.POST, instance=user)
		profile_form = ProfileForm(request.POST, instance=profile)
	return render(request, 'official/profile.html', {'user_form':user_form, 'profile_form':profile_form})


def PasswordChangeForm(request):

    if request.method == "POST":
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            try:
                request.user.set_password(form.cleaned_data['password'])
                request.user.save()
            except Exception, err:
                print "Error changing password: {}".format(err)
                messages.add_message(request, messages.ERROR, 'The password could not be changed, please try again '
                                                              'later. This admins have been notified of this error.')
            else:
                #this outputs True
                print request.user.is_authenticated()

                messages.add_message(request, messages.INFO, 'Your password has been changed successfully')
                return HttpResponseRedirect("/accounts/dashboard/")
    else:
        form = SubscriberPasswordForm()

    return render(request, "official/profile.html", {"form": form})

def addnewlisting(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect(settings.LOGIN_URL, request.path)
	listing_form = ListingForm(request.POST, request.FILES)
	
	if request.method == 'POST':
		data = {}
		listing_form = ListingForm(request.POST, request.FILES)
		request_new_listing.RequestNewListing.run(request.POST,request.FILES, data)
		save_customer_listing.SaveCustomerAd.run(data)
		messages.success(request, "Yes")
		return HttpResponseRedirect('/listings')
	else:
		listing_form = ListingForm(request.POST, request.FILES)
		return render(request,
	                  'official/create_listing.html',
	                  {'listing_form': listing_form,}, context_instance=RequestContext(request))



def listing_items(request):
	today = timezone.now().date()
	queryset_list = listing.objects.all()

	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(title__icontains=query)

	paginator = Paginator(queryset_list, 10) 
	page_request_var = "listing"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)

	context = {
		"object_list": queryset,
		"title": "List",
		"page_request_var": page_request_var,
		"today": today,
		}
		
	return render(request, "official/listings.html", context)


def listing_detail(request, id=None):
	instance = get_object_or_404(listing, id=id)
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	share_string = quote_plus(instance.description)
	context = {
		"photo": instance.photo,
		"title": instance.title,
		"instance": instance,
		"share_string": share_string,
	}
	return render(request, "official/listing_detail.html", context)

