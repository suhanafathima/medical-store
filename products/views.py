from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login
from django.contrib.auth.forms import AuthenticationForm



@login_required(login_url='/login/')
def greeting2(request):
    return render(request,'index2.html')


@login_required(login_url='/login/')
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('viewproduct')
    else:
        form =ProductForm()
    return render(request, 'create.html', {'form': form})


@login_required(login_url='/login/')
def product_read(request):
    product_list=Product.objects.all()
    return render(request,'view.html',{'product_list':product_list})


@login_required(login_url='/login/')
def product_update(request, id):
    product = Product.objects.get(pk=id)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('viewproduct')
    else:
        form =ProductForm(instance=product)           
    return render(request, 'update.html', {'form': form})

def product_delete(request,pk):
    product=Product.objects.get(pk=pk)  
    if request.method == 'POST':
        product.delete()
        return redirect('viewproduct')
    
    return render(request,'delete.html',{'product':product})



def listing(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 3)  # Set the number of items per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'list.html', {'page_obj': page_obj})

def search_medicine(request):
    if 'q' in request.GET:
        query = request.GET['q']
        medicines = Product.objects.filter(medicine_name__icontains=query)
    else:
        medicines = Product.objects.all()

    return render(request, 'search_medicine.html', {'medicines': medicines})


@login_required(login_url='/login/')
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

    context = {
        'user': request.user
    }

    return render(request, 'logout.html', context)


from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from django.contrib.auth import login 
def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Authenticate the user
            user = form.get_user()
            login(request, user)
            # Redirect to home page after successful login
            return redirect('home2')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})