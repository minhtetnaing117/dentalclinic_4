from django.shortcuts import render, redirect

from ..models import Visit,Patient
from ..form import VisitForm

def add_visit(request, patient_id):
	patient = Patient.objects.get(id=patient_id)
	owner_id = patient.owner_id.id

	if request.method == "POST":
		form = VisitForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/dentalclinic/owners/" + str(owner_id) + '/')
	else:
		form = VisitForm(initial={'patient': patient_id})
	return render(request,'visit/add.html',{'form':form})