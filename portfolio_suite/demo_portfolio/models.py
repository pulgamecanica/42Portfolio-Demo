from datetime import date
from django.db import models
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder

class User(models.Model):
	intra_username = models.CharField(max_length=30)
	intra_id = models.IntegerField(unique=True, db_index=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField(max_length=130)
	bio = models.TextField(max_length=800)
	updated_at = models.DateTimeField(auto_created=True, auto_now=True)

	def __str__(self):
		return "@" + self.intra_username

	def wasUpdatedToday(self):
		return self.updated_at > date.yesterday()

	def serialize(self):
		return serialize('json', [self])[1:-1]
