from django.shortcuts import render
from django.views import generic
from .models import CustomUser
from django.views.generic import ListView
from django.contrib.auth import get_user_model




# Create your views here.

def index(request):
    return render(request, 'index.html')

def matches(request):
    
    
    
    ##current user type
    b = request.user.user_type
    ##current user location
    c = request.user.location
    ##current user needs
    d = request.user.needs
    ## convert msfList to string for .filter()
    
    d1 = ''
    for i in d:
        d1 = d1+','+i
    
    ##filter to match users to other users(excluding themselves)
    if request.user.is_authenticated:
        user = get_user_model()
        
        if (b == 'business'):
            ##returns 'business' users results based on inputs given at sign up
            all_users = user.objects.filter(user_type__icontains='customer')
            correctusers = all_users.objects.filter(needs__icontains=d1)                           
            local_users =  correctusers.objects.filter(location__icontains=c)                         
        else:
            ##returns 'customer' user results based on inputs given at sign up
            all_users = user.objects.filter(user_type__icontains='business')
            
            correctusers = all_users.filter(needs__icontains=d1)
                                  
            local_users =  correctusers.filter(location__icontains=c) 
            
                              
           
            
       ##returns results excluding current user
        context = {'allusers': local_users.values('username','email','location','needs','user_type').exclude(username = request.user)}
        
        return render(request, 'matches.html', context)
    else:
        return render(request, 'account/signup.html')
    
    
    
    
   

    
