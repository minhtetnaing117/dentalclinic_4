from django.db import models

class PatientType(models.Model):
	Gender_Male = 'Male'
	Gender_Female = 'Female'

	Gender_Choice = [
		(Gender_Male,'Male'),
		(Gender_Female,'Female'),
	]

	name = models.CharField(max_length=30, choices=Gender_Choice, default=Gender_Male)

	def __str__(self):
		return self.name