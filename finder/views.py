from django.shortcuts import render
from django.views import generic

from django.views.generic import ListView


# Create your views here.

def index(request):
    return render(request, 'index.html')


def login_req(request):
    if request.method == 'POST':
        form = authenicationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authicate(username = username, password = password)
            if user is not None:
                login(request,user)
                return redirect("main:index")
    
    
    
   

    
