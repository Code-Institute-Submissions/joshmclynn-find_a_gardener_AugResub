from django.shortcuts import render
from django.views import generic
from .models import CustomUser
from django.views.generic import ListView
from django.contrib.auth import get_user_model


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
    currentUser = [a,b,c,d]
    print(currentUser)
    if request.user.is_authenticated:
        user = get_user_model()
        if (b == 'business'):
            all_users = user.objects.filter(user_type__icontains='customer',
                                        needs__icontains=d,
                                       location__icontains=c)
        
        else:
            all_users = user.objects.filter(user_type__icontains='business',
                                        needs__icontains=d,
                                       location__icontains=c)
       
        context = {'allusers': all_users.values('username','email','location','needs','user_type')}
        print(context)
        print(type(context))
        return render(request, 'matches.html', context)
    else:
        return render(request, 'account/signup.html')
    
    
    
    
   

    
