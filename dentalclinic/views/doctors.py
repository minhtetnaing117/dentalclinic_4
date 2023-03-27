from django.shortcuts import render
from ..models import Doctor

def all_doctors(request):
	all_doctors = Doctor.objects.all()
	context = { "all_doctors": all_doctors}
	return render(request,'doctors/all_doctors.html', context)