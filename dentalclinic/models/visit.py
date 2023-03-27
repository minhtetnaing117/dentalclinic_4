from django.db import models

from .patient import Patient
from .doctor import Doctor

class Visit(models.Model):
	visit_date = models.DateTimeField()
	description = models.TextField()
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)

	def __str__(self):
		return self.description