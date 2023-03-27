from django import forms

from .models import Owner,Patient,Visit,Appointment

class DateInput(forms.DateInput):
	input_type= 'date'

class OwnerForm(forms.ModelForm):

	class Meta:
		model = Owner
		fields = "__all__"

	def __init__(self, *args, **kwargs):
		super(OwnerForm, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'form-control'

class PatientForm(forms.ModelForm):

	class Meta:
		model = Patient
		fields = "__all__"
		widgets = {
		'birthday': DateInput(),
		'appointment': DateInput(),
		}

	def __init__(self, *args, **kwargs):
		super(PatientForm, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'form-control'

class VisitForm(forms.ModelForm):

	class Meta:
		model = Visit
		fields = "__all__"
		widgets = {'visit_date': DateInput() }



class AppointmentForm(forms.ModelForm):

	class Meta:
		model = Appointment
		fields = "__all__"
		widgets = {'appointment_date': DateInput() }

	