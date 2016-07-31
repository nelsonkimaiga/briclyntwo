class RequestDataNewListing():
	def run(request_data,request_files,data):
		
		data['new_listing_data']=RequestDataNewAd.get_data(request_data)		
		data['new_listing_file']=RequestDataNewAd.get_image(request_files)


	def get_data(request_data):
		new_listing_data ={}
		new_listing_data ['property_type']= request_data.get('property_type')
		new_listing_data['transaction_type']= request_data.get('transaction_type')
		new_listing_data['title'] = request_data.get('title')
		new_listing_data['description']= request_data.get('description')
		new_listing_data['baths'] = request_data.get('baths')
		new_listing_data['area'] = request_data.get('area')
		new_listing_data['cost'] = request_data.get('cost')
		new_listing_data['price'] = request_data.get('price')
		new_listing_data['city'] = request_data.get('city')
		new_listing_data['location'] = request_data.get('location')
		return new_listing_data


	def get_image(request_files):
		new_listing_file ={}
		new_listing_file['photo']= request_files.get('photo')
		return new_listing_file
