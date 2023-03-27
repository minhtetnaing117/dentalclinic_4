from django.shortcuts import render, redirect

from ..models import Patient
from ..form import PatientForm

def add_patient(request, owner_id):
	if request.method == "POST":
		form = PatientForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/dentalclinic/owners/" + str(owner_id) + '/')
	else:
		form= PatientForm(initial={'owner_id': owner_id})
	return render(request,'patients/add.html', {'form': form})

def edit_patient(request,patient_id):
	patient =Patient.objects.get(id=patient_id)
	form = PatientForm(initial={
		'owner_id': patient.owner_id,
		'name' : patient.name,
		'birthday' : patient.birthday,
		'patienttype' : patient.patienttype,
		'appointment' : patient.appointment,
		'marital_status' : patient.marital_status,
		})
	return render(request,'patients/update.html', {'form': form, 'patient_id':patient_id})

def update_patient(request,patient_id):
	patient =Patient.objects.get(id=patient_id)
	owner_id = patient.owner_id.id
	form = PatientForm(request.POST, instance = patient)
	if form.is_valid():
		form.save()
		return redirect('/dentalclinic/owners/' + str(owner_id) + '/')
	return render(request,'patients/update.html', {'patient': patient})