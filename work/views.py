from django.shortcuts import render
from .models import Module,Master,Sub_Module,Product


from .models import *

def index(request):
  master = Master.objects.count()
  module = Module.objects.count()
  sub_module = Sub_Module.objects.count()
  product = Product.objects.count()

  context = {
  'masters':master,
  'modules':module,
  'sub_modules':sub_module,
  'product':product,
  }

  return render(request, "index.html",context)

def starter(request):

  return render(request, "pages/starter.html")
