from django.db import models

class Owner(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	address = models.CharField(max_length=20)
	city = models.CharField(max_length=20)
	telephone = models.CharField(max_length=20)

	def __str__(self):
		return self.first_name + " " + self.last_name