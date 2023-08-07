from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserProfileForm

# Create your views here.

# Yet to add data validation.


def home(request):
    return render(request, 'home.html')


def signup(request):
     if request.method=='POST':
        user_name = request.POST.get("user_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        #print (user_name, email, password)

        profile_form = UserProfileForm(request.POST)

        my_user = User.objects.create_user(user_name, email, password)
        my_user.save()

        if profile_form.is_valid():
            profile = profile_form.save(commit = False)
            profile.user = my_user

            profile.save()

        return render(request, 'usercreated.html')

     else:
         profile_form = UserProfileForm

     context = {'profile_form' : profile_form}
     return render(request, 'signup.html', context)



def loginpage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print (username, password)

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'loginfailed.html')
        
    return render(request, 'login.html')
   

def loguserout(request):
    if request.method=="POST":
        logout(request)
        return redirect('/login/')