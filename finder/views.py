from django.shortcuts import render, redirect
from django.views import generic
from .models import CustomUser
from django.views.generic import ListView
from django.contrib.auth import get_user_model
from .forms import updateProfile
from django.contrib.auth.decorators import login_required




# Create your views here.

def index(request):
    short_locations = []
    locations = CustomUser.objects.values('location').distinct()
    short_locations = locations
    context = {'locations':short_locations}
    
    return render(request, 'index.html', context)



def matches(request):
    
    
    
    ##current user type
    b = request.user.user_type
    ##current user location
    c = request.user.location
    ##current user needs
    d = request.user.needs
    
    
    
    ##filter to match users to other users(excluding themselves)
    if request.user.is_authenticated:
        user = get_user_model()
        
        if (b == 'business'):
            ##returns 'business' users results based on inputs given at sign up
            all_users = user.objects.filter(user_type__icontains='customer')
            print(all_users)
            for i in d:
                correctusers = all_users.filter(needs__icontains=i)
            
                                         
            local_users =  correctusers.objects.filter(location__icontains=c)                         
        
        else:
            ##returns 'customer' user results based on inputs given at sign up
            all_users = user.objects.filter(user_type__icontains='business')
            
            for i in d:
                correctusers = all_users.filter(needs__icontains=i)
            
                                  
            local_users =  correctusers.filter(location__icontains=c) 
            
                              
            
       ##returns results excluding current user
        context = {'allusers': local_users.values('username','email','location','needs','user_type').exclude(username = request.user)}
        
            
        return render(request, 'matches.html', context)
    else:
        return render(request, 'account/signup.html')
    
    
    

@login_required
def profile(request):
    if request.method == 'POST':
        userform = updateProfile(request.POST, instance = request.user)
        
        if userform.is_valid():
            userform.save()
            return redirect(to='index')
    else:
        user_form = updateProfile(instance= request.user)
        
    
    return render(request, 'profile.html', {'user_form': user_form})
            