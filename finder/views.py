from django.shortcuts import render, redirect
from django.views import generic
from .models import CustomUser
from django.views.generic import ListView
from django.contrib.auth import get_user_model
from .forms import update_profile
from django.contrib.auth.decorators import login_required
import sweetify


# view to return current cities users are located in.
def index(request):
    short_locations = []
    locations = CustomUser.objects.values('location').distinct()
    short_locations = locations
    context = {'locations': short_locations}

    return render(request, 'index.html', context)


# function returns other users based on a number of
# attributes that would link the
# logged in user to the selected users.
def matches(request):

    # current user type
    b = request.user.user_type
    # current user location
    c = request.user.location
    # current user needs
    d = request.user.needs

    # filter to match users to other users(excluding themselves)
    if request.user.is_authenticated:
        user = get_user_model()

        if (b == 'business'):
            # returns 'business' users results based on inputs given at sign up
            all_users = user.objects.filter(user_type__icontains='customer')
            print(all_users)

            for i in d:
                correctusers = all_users.filter(needs__icontains=i)

                local_users = correctusers.objects.filter(
                                                    location__icontains=c)

        else:
            # returns 'customer' user results based on inputs given at sign up
            all_users = user.objects.filter(user_type__icontains='business')
            for i in d:
                correctusers = all_users.filter(needs__icontains=i)

                local_users = correctusers.filter(location__icontains=c)

        # returns results excluding current user
        context = {'allusers': local_users.values('username', 'email',
                                                  'location',
                                                  'needs', 'user_type')
                   .exclude(username=request.user).exclude(
                                                username='find-a-gardener')}

        if(local_users.count() == 0):
            sweetify.warning(request, """Unfortunately there is no one else
                             in your area at the minute, try again soon!""")

        return render(request, 'matches.html', context)

    else:
        return render(request, 'account/signup.html')


# function to change the current logged in users profile attributes
@login_required
def profile(request):
    if request.method == 'POST':
        userform = update_profile(request.POST, instance=request.user)

        if userform.is_valid():
            userform.save()
            sweetify.success(request, title='Your profile has been updated!')
            return redirect(to='index')
    else:
        user_form = update_profile(instance=request.user)

    return render(request, 'profile.html', {'user_form': user_form})


# Function for the user to delete their account
@login_required
def delete(request):
    try:
        a = CustomUser.objects.get(username=request.user.username)
        a.delete()
        sweetify.success(request, title='Your profile has been deleted!')
    except CustomUser.DoesNotExist:
        sweetify.error(request, title='Profile does not exist')

    return redirect(to='index')
