from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'base.html')

def feed(request) :
    return render(request,'feed.html')

def login(request) :
    return render(request,'login.html')
    
def profile(request) :
    return render(request,'profile.html')
    
def signup(request) :
    return render(request,'signup.html')
    

def new(request) :
    return render(request,"new.html")