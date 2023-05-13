from django.shortcuts import render, redirect
from . models import Product

# Importing my form into ma view
from . forms import ProductForm

# Create your views here.


# Function for diaplaying all products to the user
def showAllProduct(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'showallproducts.html', context)


# Function shwoing details of a single product selected by customer basingg on its ID
def productDetail(request, pk):
    eachproduct = Product.objects.get(id=pk)
    context ={
        'eachproduct': eachproduct
    }
    return render(request, 'productdetail.html', context)

# Function for adding New products to the DB
def addProduct(request):
    form = ProductForm
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("showProducts")
    else:
        form = ProductForm()
    context ={
        "form":form
    }
    return render(request, 'addproduct.html', context)
    


# Function for Updating selected products to the DB
def updateProduct(request, pk):
    # getting each product from DB basing on PK selected
    product = Product.objects.get(id=pk)

    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("showProducts")
    else:
        form = ProductForm()
    context = {
        "form":form
    }
    return render(request, 'updateproduct.html', context)

# Function to delete a product
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect('showProducts')