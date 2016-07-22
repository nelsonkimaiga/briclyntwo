from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms
from .models import *


#-------------------------------------------------------------------------------------

class UserForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'username', 'password')

#-------------------------------------------------------------------------------------

class ProfileForm(forms.ModelForm):

	class Meta:
		model = UserProfile
		fields = ('phone',)


class ListingForm(forms.ModelForm):

	class Meta:
		model = listing
		fields = ('property_type', 'transaction_type', 'title', 'description', 'baths', 'area', 'cost', 'price', 'city', 'location', 'photo')