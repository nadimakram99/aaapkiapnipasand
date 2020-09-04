from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import contact


def index(request):
    # return HttpResponse("this is a homepage nadim")
    return render(request,'index.html')

def about(request):
   return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def  Contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()

    return render(request, 'contact.html')
