from django.shortcuts import render, redirect

from ..models import Owner
from ..form import OwnerForm
# Create your views here.

def owner(request,owner_id):
	owner = Owner.objects.get(pk=owner_id)
	return render(request,'owners/detail.html',{'owner': owner})

def all_owners(request):
	if 'last_name' in request.GET:
		all_owners = Owner.objects.filter(last_name__icontains=request.GET['last_name'])
	else:
		all_owners = Owner.objects.all()
	context = { "all_owners": all_owners}
	return render(request,'owners/list.html', context)

def find_owner(request):
	return render(request,'owners/find.html', {})

def add_owner(request):
	if request.method == "POST":
		form = OwnerForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/dentalclinic/owners')
	else:
		form= OwnerForm()
	return render(request,'owners/add.html', {'form': form})

def edit_owner(request,owner_id):
	owner =Owner.objects.get(id=owner_id)
	return render(request,'owners/update.html', {'owner': owner})

def update_owner(request,owner_id):
	owner =Owner.objects.get(id=owner_id)
	form = OwnerForm(request.POST, instance = owner)
	if form.is_valid():
		form.save()
		return redirect('/dentalclinic/owners/' + str(owner_id) + '/')
	return render(request,'owners/update.html', {'owner': owner})
