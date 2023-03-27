from django.contrib import admin

# Register your models here.
from .models import *

class PatientTypeAdmin(admin.ModelAdmin):
	list_display = ['name']
admin.site.register(PatientType,PatientTypeAdmin)

class PatientAdmin(admin.ModelAdmin):
	list_display = ['owner_id','name','doctor_id','patienttype','birthday','appointment','marital_status']
admin.site.register(Patient,PatientAdmin)

class OwnerAdmin(admin.ModelAdmin):
	fieldsets = (
		("Section 1",
			{'fields':('first_name','last_name',)
		}),
		("Section 2",
			{'fields':('address',)
		}),
		("Section 3",
			{'fields':('city',)
		}),
		("Section 4",
			{'fields':('telephone',)
		}),
	)
admin.site.register(Owner,OwnerAdmin)

class SpecialtyAdmin(admin.ModelAdmin):
	list_display = ['name']
admin.site.register(Specialty,SpecialtyAdmin)

class DoctorAdmin(admin.ModelAdmin):
	list_display = ['first_name','last_name','mbbs']
admin.site.register(Doctor,DoctorAdmin)

class VisitAdmin(admin.ModelAdmin):
	list_display = ['visit_date','description','patient','doctor_id']
admin.site.register(Visit,VisitAdmin)

# class AppointmentAdmin(admin.ModelAdmin):
# 	fieldsets = (
# 		("Section 1",
# 			{'fields':('appointment_date',)
# 		}),
# 	)
# admin.site.register(Appointment,AppointmentAdmin)