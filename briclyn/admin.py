from django.contrib.auth.models import User
from django.contrib import admin
from .models import *


class ListingAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "title", "price"]
	search_fields = ["title", "description"]
	class Meta:
		model = listing

class CustomerAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "phone"]
	search_fields = ["phone"]
	class Meta:
		model = UserProfile



admin.site.register(listing, ListingAdmin)
admin.site.register(UserProfile, CustomerAdmin)
