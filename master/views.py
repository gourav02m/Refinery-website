from django.shortcuts import render, redirect,get_object_or_404
from .models import Master
import datetime
from django.utils.dateparse import parse_datetime
# from .models import *

# Create your views here.
def master_form(request):

  if request.method == 'POST':
        # plantid = request.POST.get('plantid')
        date = datetime.datetime.now()
        # start_time = parse_datetime(date)
        plantname = request.POST.get('plantname')
        planttype = request.POST.get('planttype')
        plantmanagername = request.POST.get('plantmanagername')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        phonenumber = request.POST.get('phonenumber')
        email = request.POST.get('email')
        plantcapacity = request.POST.get('plantcapacity')
        establishment = request.POST.get('establishment')
        certification = request.POST.get('certification')
        operatinghours = request.POST.get('operatinghours')
        if planttype:
            master = Master.objects.create(date_time=date, plant_name=plantname, plant_type =planttype ,
              manager_name =plantmanagername ,address_1 =address1 ,address_2 =address2 ,city =city ,
              state =state,phone_number =phonenumber,email =email, capacity =plantcapacity,
              establishment =establishment,compliance_certification =certification,operating_hours =operatinghours )
            # messages.success(request, "Title created successfully!")
            return redirect('master_list')
        else:
            print("Topic Title is required.")
            # messages.error(request, "Topic Title is required.")

  return render(request, "master_form.html")

def master_list(request):

  m_list = Master.objects.all()
  return render(request, "master_list.html", {'lists' : m_list})

def remove_master(request, plant_id):
  print(f"Received ID: {plant_id}")
  item = get_object_or_404(Master, plant_id=plant_id)
  item.delete()
  # messages.info(request, "Removed successfully!")
  return redirect('master_list')

def master_edit(request, plant_id):
  master = Master.objects.filter(plant_id=plant_id)
  if request.method == 'POST':
    master.update(
      plant_name = request.POST.get('plantname'),
      plant_type = request.POST.get('planttype'),
      manager_name = request.POST.get('plantmanagername'),
      address_1 = request.POST.get('address1'),
      address_2 = request.POST.get('address2'),
      city = request.POST.get('city'),
      state = request.POST.get('state'),
      phone_number = request.POST.get('phonenumber'),
      email = request.POST.get('email'),
      capacity = request.POST.get('plantcapacity'),
      establishment = request.POST.get('establishment'),
      compliance_certification = request.POST.get('certification'),
      operating_hours = request.POST.get('operatinghours'))

    return redirect('master_list')
    
  return render(request,"master_edit.html", {'lists' : master})