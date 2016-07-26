from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render,render_to_response, get_object_or_404
from django.template import RequestContext

from .models import *
from briclyn.forms import *



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