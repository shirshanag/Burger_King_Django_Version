from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(requests):
    return render(requests,'index.html')
def about(requests):
    return render(requests,'about.html')
def blog(requests):
    return render (requests,'blog.html')
def booking(requests):
    return render(requests,'booking.html')
def contact(requests):
    return render(requests,'contact.html')
def feature(requests):
    return render(requests,"feature.html")
def menu(requests):
    return render(requests,"menu.html")
def single(requests):
    return render (requests,"single.html")
def team(requests):
    return render(requests,"team.html")