from django.db import models

class Appointment(models.Model):
	appointment_date = models.DateTimeField()

	def __str__(self):
		return self.appointment_date