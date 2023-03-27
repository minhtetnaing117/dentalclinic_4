from django.db import models
from .owner import Owner
from .patienttype import PatientType
from .doctor import Doctor
# from .appointment import Appointment

class Patient(models.Model):
	Marital_Status_Single = 'Single'
	Marital_Status_Married = 'Married'
	Marital_Status_Divorced = 'Divorced'
	Marital_Status_Widowed = 'Widowed'

	Marital_Status_Choices = [
		(Marital_Status_Single,'Single'),
		(Marital_Status_Married,'Married'),
		(Marital_Status_Divorced,'Divorced'),
		(Marital_Status_Widowed,'Widowed'),

	]

	name = models.CharField(max_length=30)
	owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE)
	doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
	patienttype_id = models.ForeignKey(PatientType, name='patienttype', on_delete=models.CASCADE)
	birthday = models.DateTimeField(name='birthday',default=None)
	appointment = models.DateTimeField(name='appointment',default=None)
	marital_status = models.CharField(max_length=30 , choices=Marital_Status_Choices, default=Marital_Status_Single, name='marital_status')

	def __str__(self):
		return self.name