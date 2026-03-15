from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def blog(request):
    return render (request,'blog.html')
def booking(request):
    if request.method=="POST":
        a1=request.POST['name']
        a2=request.POST['email']
        a3=request.POST['mobile']
        a4=request.POST['date']
        a5=request.POST['time']
        a6=request.POST['guests']
        from .models import Book_data
        data=Book_data(name=a1,email=a2,mobile=a3,date=a4,time=a5,guests=a6)
        data.save()

    return render(request,'booking.html')
def contact(request):
    return render(request,'contact.html')
def feature(request):
    return render(request,"feature.html")
def menu(request):
    return render(request,"menu.html")
def single(request):
    return render (request,"single.html")
def team(request):
    return render(request,"team.html")
