from django.shortcuts import render
from . models import *
# Create your views here.
def fnindex(request):
    if (request.method=='POST'):
        print("sign in")
        f_name=request.POST.get('f_name')
        s_name=request.POST.get('s_name')
        username=request.POST.get('username')
        password=request.POST.get('password')
        day=request.POST.get('day')
        month=request.POST.get('month')
        year=request.POST.get('year')
        if day!=None and month!=None and year!=None:
            dob=day+"-"+month+"-"+year
        gender=request.POST.get('gender') 
        print(f_name,s_name,username,password,dob)
        loginobj=Login(username=username,password=password)
        loginobj.save()
        registerdata=Users(f_name=f_name,s_name=s_name,dob=dob,gender=gender,user_id=loginobj)
        registerdata.save()
        print("Sign in successful")
        return render(request,'home.html')
    else:
        return render(request,'index.html')
def fnhome(request):
    return render(request,'home.html')
