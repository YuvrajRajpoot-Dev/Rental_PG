from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
def home(request):
    if request.user.is_anonymous:
        return redirect('/userlogin')

    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username,password= password)
        if user is not None:
        # A backend authenticated the credentials
            return redirect('/')
        else:
        # No backend authenticated the credentials
            return render(request, 'login.html')


    return render(request, 'login.html')
