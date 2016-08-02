from django.http import HttpResponseRedirect, HttpResponse
from briclyn.models import listing
from django.utils import timezone
from datetime import *
from datetime import datetime


class SaveCustomerAd():
	def run(data):
		new_listing_data = data.get('new_listing_data')
		save_listing_data = listing(**new_listing_data)
		new_listing_file = data.get('new_listing_file')
		save_image= listing(**new_listing_file)

		property_type= save_listing_data.property_type
		transaction_type = save_listing_data.transaction_type
		title=save_listing_data.title
		description = save_listing_data.description
		baths =save_listing_data.baths
		bedrooms =save_listing_data.bedrooms
		area=save_listing_data.area
		cost=save_listing_data.cost
		price = save_listing_data.price
		city = save_listing_data.city
		location = save_listing_data.location
		photo = save_image.photo
		# created_at = datetime.strptime(created_at, "%d/%m/%Y")
		# end_date = datetime.strptime(end_date, "%d/%m/%Y")
		sav =listing(property_type=property_type, transaction_type=transaction_type,title=title, description=description, baths=baths, bedrooms=bedrooms, area=area,cost=cost, price=price, city=city, location=location, photo=photo)
		sav.save()
		data['sav']=sav
		data['save_listing_data']= save_listing_data
		
