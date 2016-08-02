from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms
from django.forms import ModelForm
from .models import *


#-------------------------------------------------------------------------------------

class UserForm(ModelForm):

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'username')

#-------------------------------------------------------------------------------------
class PasswordChangeForm(forms.Form):
	password = forms.CharField(widget=forms.PasswordInput)
	cpassword = forms.CharField(widget=forms.PasswordInput)


	def clean_password2(self):
		password1 = self.cleaned_data.get("password")
		password2 = self.cleaned_data.get("cpassword")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError(
				self.error_messages['password_mismatch'],
				code='password_mismatch',
				)

#---------------------------------------------------------------------------------------------






#---------------------------------------------------------------------------------------------


class ProfileForm(ModelForm):

	class Meta:
		model = UserProfile
		fields = ('phone',)

#---------------------------------------------------------------------------------------------


class ListingForm(ModelForm):

	class Meta:
		model = listing
		fields = ('property_type', 'transaction_type', 'title', 'description', 'baths', 'bedrooms', 'area', 'cost', 'price', 'city', 'location', 'photo')


#---------------------------------------------------------------------------------------------

