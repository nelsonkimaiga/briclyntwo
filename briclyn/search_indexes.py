import datetime
from haystack import indexes
from .models import listing



class ListingIndex(indexes.SearchIndex, indexes.Indexable):
	property_type = indexes.CharField(document=True, use_template=True)
	transaction_type = indexes.CharField(model_attr='transaction_type')
	cost = indexes.IntegerField(model_attr='cost')
	price = indexes.CharField(model_attr='price')
	city= indexes.CharField(model_attr='city')

	def get_model(self):
		return listing


	def index_queryset(self, using=None):
		return self.get_model().objects.all()