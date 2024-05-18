from django.shortcuts import render
from .forms import LoginModelForm

def greeting(request):
    return render(request,'index.html')

from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from django.contrib.auth import login 

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Authenticate the user
            user = form.get_user()
            login(request, user)
            # Redirect to home page after successful login
            return redirect('home2')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
 
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            # Redirect to login page after successful signup
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

