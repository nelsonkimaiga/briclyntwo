# from adlink.models import clerk_auth
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
class SendAdEmail():
	def run (data):
		new_listing_data = data.get('new_listing_data')
		user = request.user
		
		subject ="Your Listing was created succesfully"
		subject, from_email, to = subject, settings.EMAIL_HOST_USER, user.email
		text_content = 'Your Briclyn Listing has been added'
		html_content = "<p>This is your <strong>briclyn</strong>"
		msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
		msg.attach_alternative(html_content, "text/html")
		msg.send()






		
		
		
	
