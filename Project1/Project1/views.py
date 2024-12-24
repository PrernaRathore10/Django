'''allows you to return an HTTP response in Django views. 
It is used to send data (such as text or HTML) back to 
the client’s browser.'''
from django.http import HttpResponse
from django.shortcuts import render

def home (request):
    # return HttpResponse("Hello World. You are at chai aur django home page")
    return render(request,'index.html')
def about (request):
    # return HttpResponse("Hello World. You are at chai aur django about page")
    return render(request,'about.html')
def contact (request):
    # return HttpResponse("Hello World. You are at chai aur django contact page")
    return render(request,'contact.html')
