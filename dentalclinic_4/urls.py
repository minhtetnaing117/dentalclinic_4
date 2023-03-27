"""dentalclinic_4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from dentalclinic import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('dentalclinic/', views.index),

    path('dentalclinic/owners/', views.all_owners),
    path('dentalclinic/owners/find/', views.find_owner),
    path('dentalclinic/owners/<int:owner_id>/', views.owner),
    path('dentalclinic/owners/add/', views.add_owner),
    path('dentalclinic/owners/edit/<int:owner_id>/', views.edit_owner),
    path('dentalclinic/owners/update/<int:owner_id>/', views.update_owner),

    path('dentalclinic/patients/add/<int:owner_id>/', views.add_patient),
    path('dentalclinic/patients/edit/<int:patient_id>/', views.edit_patient),
    path('dentalclinic/patients/update/<int:patient_id>/', views.update_patient),

    path('dentalclinic/visit/add/<int:patient_id>/', views.add_visit),

    path('dentalclinic/doctors/', views.all_doctors),
    
    path('dentalclinic/about/', views.about),

]