from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import userForm
from data.models import user
from service.models import Service
from service.models import About
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import HttpResponseRedirect

def homePage(request):
    return HttpResponse("<h1>Welcome to my practise setion</h1>")

def student(request,id):
    return HttpResponse(id)

def home(request):
    if request.user.is_authenticated:
      data={
        'p':'hi my name is <h2>pratik sarvate</h2> and i am trying to send data to html file from views.py ',
        'student':["Rahul","Aman","Ram"],
      }
      return render(request,"home.html",data)
    else:
        return HttpResponseRedirect('/login')

def aboutus(request):
    serviceData=Service.objects.all().order_by('ser_title')
    aboutData=About.objects.all()
    if request.method=="GET":
        st=request.GET.get('ser_title')
        if st!=None:
            serviceData=Service.objects.filter(ser_title__icontains=st)
    paginator=Paginator(serviceData,2)
    pg_num=request.GET.get('page')
    final=paginator.get_page(pg_num)
    data={
        'serviceData':final,
        'aboutData':aboutData
    }
    return render(request,"aboutus.html",data)

def thankYou(request):
    return render(request,"thankyou.html")

def userForms(request):
    fn=userForm()
    if request.method=="POST":
        n=request.POST.get('Name')
        c=request.POST.get('Contact')
        e=request.POST.get('Email')
        a=request.POST.get('Address')

        data=user(
            name=n,
            contact=c,
            email=e,
            adress=a
        )
        data.save()
        return HttpResponseRedirect('/thank-you/')
    return render(request,"userform.html",{'form':fn})


def usersignup(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        upass=request.POST.get('password')

        user=User.objects.create_user(
            username=uname,
            password=upass
        )
        user.save()
        return HttpResponseRedirect('/login/')
    return render(request,"signup.html")



def userlogin(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        upass=request.POST.get('password')

        user=authenticate(
            username=uname,
            password=upass
        )
        if user is not None:
            login(request,user)
        return HttpResponseRedirect('/dashboard/')
    return render(request,'login.html')
    
def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'dashboard.html')
    else:
        return HttpResponseRedirect('/login/')
    
def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/login/')