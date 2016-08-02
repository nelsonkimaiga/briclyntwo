from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from allauth.account.models import EmailAddress

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User, related_name='profile')
	phone = models.CharField(max_length=100, unique=False, blank=True, null=True)

	def __unicode__(self):
		return "{}'s profile".format(self.user.username)

	class Meta:
		db_table = 'user_profile'

	def account_verified(self):
		if self.user.is_authenticated:
			result = EmailAddress.objects.filter(email=self.user.email)
			if len(result):
				return result[0].verified
		return False
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

PROPERTY_CHOICES = (
	('HOUSE', 'House'),
	('OFFICE', 'Office'),
	('APARTMENT', 'Apartment'),
	)

TRANSACTION_CHOICES = (
	('RENT', 'Rent'),
	('SALE', 'Sale'),
	)



class listing(models.Model):
	property_type = models.CharField(max_length=100, unique=False, blank=True, choices=PROPERTY_CHOICES)
	transaction_type = models.CharField(max_length=100, unique=False, blank=True, choices=TRANSACTION_CHOICES)
	title = models.CharField(max_length=250, unique=False, blank=True)
	description = models.CharField(max_length=250, unique=False, blank=False)
	baths = models.IntegerField(default=0, null=True, blank=True)
	bedrooms = models.IntegerField(default=0, null=True, blank=True)
	area = models.CharField(max_length=100, default=0)
	cost = models.IntegerField(default=0, blank=True, null=True)
	price = models.DecimalField(max_digits=9,decimal_places=2, default=0, null=True, blank=True)
	city= models.CharField(max_length=100, unique=False,blank=True)
	location= models.CharField(max_length=100, unique=False,blank=True)
	photo =models.FileField(upload_to="documents/%Y/%m/%d", null=True)

	def __unicode__(self):
		return '%s' %self.title


	def __str__(self):
		return self.title


# class emailResponse(models.Model):
# 	first_name = models.CharField()
# 	last_name = models.CharField()
# 	email = models.EmailField()
# 	message = models.CharField()