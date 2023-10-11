from django.http import HttpResponse
from django.shortcuts import render
from storeapp.models import Product


def dashboard(request):
    return render(request,'dashboard.html')

def home(request):
    products =Product.objects.all().filter(is_available=True)
    context = {

      'products':products,
    }
    return render(request,'home.html',context)

def Get_data(request):
    return render(request,'Get_data')
