from django.shortcuts import render,redirect, get_object_or_404
from .models import Module,Master

# Create your views here.
def module_form(request):
  if request.method == 'POST':
        # warehouseid = request.POST.get('warehouseid')
        warehousename = request.POST.get('warehousename')
        associatedplant = request.POST.get('associatedplant')
        warehousemanagername = request.POST.get('warehousemanagername')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        phonenumber = request.POST.get('phonenumber')
        email = request.POST.get('email')
        storagecapacity = request.POST.get('storagecapacity')
        temperaturecontrol = request.POST.get('temperaturecontrol')
        hazardousmaterial = request.POST.get('hazardousmaterial')
        securityfeatures = request.POST.getlist('securityfeatures')
        if associatedplant:
            module = Module.objects.create( warehouse_name=warehousename, associated_plant =associatedplant ,
              manager_name =warehousemanagername ,address_1 =address1 ,address_2 =address2 ,city =city ,
              state =state,phone_number =phonenumber,email =email, storage_capacity =storagecapacity,
              temperature_control =temperaturecontrol,hazardous_material =hazardousmaterial,securityfeatures =",".join(securityfeatures) )
            # messages.success(request, "Title created successfully!")
            return redirect('module_list')
        else:
            messages.error(request, "Topic Title is required.")
  master = Master.objects.all()
  return render(request, "module_form.html", {'masters':master})

def module_list(request):

  m_list = Module.objects.all()
  return render(request, "module_list.html", {'lists' : m_list})

def remove_module(request, warehouse_id):
  item = get_object_or_404(Module, warehouse_id=warehouse_id)
  item.delete()
  return redirect('module_list')

def module_edit(request, warehouse_id):
  module = Module.objects.filter(warehouse_id = warehouse_id)
  if request.method == 'POST':
    module.update(
      warehouse_name = request.POST.get('warehousename'),
      associated_plant = request.POST.get('associatedplant'),
      manager_name = request.POST.get('warehousemanagername'),
      address_1 = request.POST.get('address1'),
      address_2 = request.POST.get('address2'),
      city = request.POST.get('city'),
      state = request.POST.get('state'),
      phone_number = request.POST.get('phonenumber'),
      email = request.POST.get('email'),
      storage_capacity = request.POST.get('storagecapacity'),
      temperature_control = request.POST.get('temperaturecontrol'),
      hazardous_material = request.POST.get('hazardousmaterial'),
      securityfeatures = request.POST.getlist('securityfeatures'))

    return redirect('module_list')
    
  return render(request,"module_edit.html", {'lists' : module})