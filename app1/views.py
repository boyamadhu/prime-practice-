from django.shortcuts import render

# Create your views here.
def sam(request):
    return render(request,'first.html')

def prime_login(request):
    return render(request,'prime_login.html')

def second(request):
    return render(request,'second.html')

def prime_plans(request):
    return render(request,'prime_plans.html')

def channels(request):
    return render(request,'channels.html')

