from django.shortcuts import render,redirect,get_object_or_404
from .models import Product,Master,Module,Sub_Module
# from .forms import ProductForm
from django.contrib import messages
import qrcode
from io import BytesIO
from django.core.files import File
from django.http import JsonResponse



def generate_qr_code(data):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    return img


def product_form(request):

    if request.method == 'POST':
        productname = request.POST.get('productname')
        productquantity = request.POST.get('productquantity')
        # created = request.POST.get('created')
        productallocation = request.POST.get('productallocation')
        productdescription = request.POST.get('productdescription')

        if productname:
            product = Product.objects.create(
                product_name=productname,
                product_quantity=productquantity,
                # created_by=created,
                product_allocation=productallocation,
                product_description=productdescription
            )

            qr_data = f"Product Name: {productname}\nQuantity: {productquantity}\nAllocation: {productallocation}\nDescription: {productdescription}"
            
            qr_img = generate_qr_code(qr_data)

            buffer = BytesIO()
            qr_img.save(buffer, format='PNG')
            buffer.seek(0)

            
            filename = f'qr_{product.id}.png'
            product.qr_code_image.save(filename, File(buffer), save=True)

            messages.success(request, "Product saved and QR code generated.")
            return redirect('product_form')  # Redirect after saving
        else:
            messages.error(request, "Product name is required.")
    products = Product.objects.filter().order_by('-created_on').first()
    masters = Master.objects.all()
    modules = Module.objects.all()
    sub_modules = Sub_Module.objects.all()

    return render(request, 'product_form.html',{'products':products,'masters':masters,'modules':modules,'sub_modules':sub_modules})

def product_list(request):
    query = request.GET.get('search', '')
    if query:
        product = Product.objects.filter(product_name__icontains=query)
    else:
        product = Product.objects.all()

    return render(request,"product_list.html",{'product':product})

def remove_product(request, id):
    print(f"Received ID: {id}")
    item = get_object_or_404(Product, id=id)
    item.delete()
    # messages.info(request, "Removed successfully!")
    return redirect('product_list')

# def get_modules(request):
#     master_name = request.GET.get('master_name')  # Get the selected master name
#     modules = Module.objects.filter(associated_plant=master_name)  # Filter Modules by plant name
#     module_list = list(modules.values('id', 'name'))  # Convert to list of dictionaries
#     return JsonResponse({'modules': module_list})  # Return JSON response

# def get_sub_modules(request):
#     module_name = request.GET.get('module_name')  # Get the selected module name
#     sub_modules = Sub_Module.objects.filter(associated_warehouse=module_name)  # Filter Sub-Modules by module name
#     sub_module_list = list(sub_modules.values('id', 'name'))  # Convert to list of dictionaries
#     return JsonResponse({'sub_modules': sub_module_list})  # Return JSON response