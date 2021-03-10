from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Leave
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    data=Leave.objects.all()
    print(data)
    return render(request,'index.html',{'data':data})

def manageleave(request):
    if request.method=='POST':
        start_date=request.POST.get('startdate')
        end_data=request.POST.get('enddata')
        description=request.POST.get('reason')
        total_days = request.POST.get('totaldays')
        user_id = User.objects.get(username=request.user)
        print("total_days=============",total_days)
        Leave.objects.create(description=description,start_date=start_date,end_data=end_data,total_days=total_days,user_id=user_id.id)
    return render(request,'leave.html')

def Register(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        x=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
        x.save()
        return redirect('home:home')
    else:
        return render(request,'index.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home:home')
        else:
            return redirect('home:home')
    else:
        return render(request, 'home.html')

def UserLogout(request):
    logout(request)
    return redirect('home:home')