from django.db import models

from .specialty import Specialty

class Doctor(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	mbbs = models.CharField(max_length=200)
	specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)

	def __str__(self):
		return self.first_name + " " + self.last_name