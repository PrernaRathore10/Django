'''allows you to return an HTTP response in Django views. 
It is used to send data (such as text or HTML) back to 
the client’s browser.'''
from django.http import HttpResponse

def home (request):
    return HttpResponse("Hello World. You are at chai aur django home page")
def about (request):
    return HttpResponse("Hello World. You are at chai aur django about page")
def contact (request):
    return HttpResponse("Hello World. You are at chai aur django contact page")
