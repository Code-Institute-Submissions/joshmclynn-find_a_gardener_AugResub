from django.shortcuts import render
from django.views import generic
from finder.models import customer
from django.views.generic import ListView

# Create your views here.

def index(request):
    return render(request, 'index.html')

   
def business_reg(request):
    return render(request, 'busi_registration.html')
    
def customer_reg(request):
    return render(request, 'cust_registration.html')
