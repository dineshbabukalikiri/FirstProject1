from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
data=[1,2,3,4.5]

def home(req):
    return HttpResponse("Home") 
def about(req):
    return HttpResponse("about")
def aboutIndex(req):
    print("id : ",id)
    return HttpResponse(f"About ")