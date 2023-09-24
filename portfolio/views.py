from django.shortcuts import render
from .models import Userr

def index(request):
    return render(request,'portfolio/index.html')

def submit(request):
    if request.method=="POST":
        u=Userr()
        name=request.POST.get('name')
        email=request.POST.get('email')
        msgg=request.POST.get('comment')
        u.name=name
        u.email=email
        u.message=msgg
        u.save()
    return render(request,'portfolio/submit.html')

# Create your views here.
