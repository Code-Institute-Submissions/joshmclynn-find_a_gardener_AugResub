from django.shortcuts import render
from django.views import generic
from finder.models import customer
from django.views.generic import ListView
from .forms import business_form, customer_form

# Create your views here.

def index(request):
    return render(request, 'index.html')

   
def business_reg(request):
    if request.method == 'POST':
        businessForm = business_form(request.POST , request.FILES)
        if businessForm.is_valid():
            businessForm.save()
            
        
            

        
    businessForm = business_form()

    return render(request, 'busi_registration.html', context={'businessForm':businessForm})


    
def customer_reg(request):
    if request.method == 'POST':
        customerForm = customer_form(request.POST , request.FILES)
        if customerForm.is_valid():
            customerForm.save()
            
        
            

        
    customerForm = customer_form()

    return render(request, 'cust_registration.html', context={'customerForm':customerForm})
    
