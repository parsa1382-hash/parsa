from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
	name = models.CharField(max_length=200)
	user = models.ManyToManyField(User)

	def __str__(slef):
		return self.name