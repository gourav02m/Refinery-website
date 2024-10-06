from django.shortcuts import render,redirect, get_object_or_404
from .models import Sub_Module,Module

# Create your views here.
def submodule_form(request):
  if request.method == 'POST':
        # sectionid = request.POST.get('sectionid')
        sectionname = request.POST.get('sectionname')
        associatedwarehouse = request.POST.get('associatedwarehouse')
        sectioncapacity = request.POST.get('sectioncapacity')
        temperaturerequirements = request.POST.get('temperaturerequirements')
        specialhandling = request.POST.get('specialhandling')
        sectiontype = request.POST.get('sectiontype')
        storeditem = request.POST.get('storeditem')
        accesscontrol = request.POST.get('accesscontrol')
        safetyrequirements = request.POST.getlist('safetyrequirements')
        if associatedwarehouse:
            sub_module = Sub_Module.objects.create(section_name =sectionname ,
              associated_warehouse =associatedwarehouse ,section_capacity =sectioncapacity,temperature_requirement =temperaturerequirements,
              special_handling =specialhandling, section_type =sectiontype,stored_item_types =storeditem,
              access_control =accesscontrol,safety_requirements =",".join(safetyrequirements) )
            return redirect('sub_module_list')
        else:
          print("error")
            # messages.error(request, "Topic Title is required.")
  module = Module.objects.all()
  return render(request, "submodule_form.html",{'modules': module})

def sub_module_list(request):

  m_list = Sub_Module.objects.all()
  return render(request, "sub_module_list.html", {'lists' : m_list})

def remove_sub_module(request, section_id):
  item = get_object_or_404(Sub_Module, section_id=section_id)
  item.delete()
  return redirect('sub_module_list')


def sub_module_edit(request, section_id):
  sub_module = Sub_Module.objects.filter(section_id = section_id)
  if request.method == 'POST':
    sub_module.update(
      section_name = request.POST.get('sectionname'),
      associated_warehouse = request.POST.get('associatedwarehouse'),
      section_type = request.POST.get('sectiontype'),
      section_capacity = request.POST.get('sectioncapacity'),
      temperature_requirement = request.POST.get('temperaturerequirements'),
      special_handling = request.POST.get('specialhandling'),
      stored_item_types = request.POST.get('storeditem'),
      access_control = request.POST.get('accesscontrol'),
      safety_requirements = request.POST.get('safetyrequirements'))

    return redirect('sub_module_list')
    
  return render(request,"sub_module_edit.html", {'lists' : sub_module})