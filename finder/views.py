from django.shortcuts import render
from django.views import generic
from .models import CustomUser
from django.views.generic import ListView
from django.contrib.auth import get_user_model
from django.db.models import Q


# Create your views here.

def index(request):
    return render(request, 'index.html')

def matches(request):
    currentUser = []
    ##current user username
    a = request.user
    ##current user type
    b = request.user.user_type
    ##current user location
    c = request.user.location
    ##current user needs
    d = request.user.needs
    ## convert msfList to string for .filter()
    d1 = ""
    for i in d:
        d1 = d1+i
        
    
    currentUser = [a,b,c,d]

    if request.user.is_authenticated:
        user = get_user_model()
        
        if (b == 'business'):
            all_users = user.objects.filter(Q(user_type__icontains='customer')|
                                        Q(needs__icontains=d1)|
                                       Q(location__icontains=c))
        else:
            
            all_users = user.objects.filter(needs__icontains=d1,user_type__icontains='business',location__icontains=c)                       
           
            print(all_users)
       
        context = {'allusers': all_users.values('username','email','location','needs','user_type').exclude(username = request.user)}
        
        return render(request, 'matches.html', context)
    else:
        return render(request, 'account/signup.html')
    
    
    
    
   

    
