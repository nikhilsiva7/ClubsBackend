from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from events.models import EventRegistration


# Create your views here.

def home(request):
    return render(request,'home.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')
    


def register(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST[('password')]
        # role=request.POST['role']


        if User.objects.filter(username=username).exists():
            messages.info(request,'Username already exists....')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email already exists....')
            return redirect('register')
        else:       
            user=User.objects.create_user(first_name=name,email=email,username=username,password=password) 
            user.save()
            return redirect('/')
    else:
        return render(request,'register.html')
    
def profile(request):
    reg_events=EventRegistration.objects.filter(user=request.user).select_related("event")
    return render(request,'profile.html',{'reg_events':reg_events})
    
def logout(request):
    auth.logout(request)
    return redirect('/')