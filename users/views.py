from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.shortcuts import render, redirect
from .forms import UserSignupForm, UserSigninForm
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = UserSignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserSigninForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page, e.g., dashboard
                return redirect('dashboard')
            else:
                # Invalid login
                form.add_error(None, "Invalid username or password.")
    else:
        form = UserSigninForm()

    return render(request, 'login.html', {'form': form})
@login_required
def dashboard(request):
    data = CustomUser.objects.filter(user=request.user).values()
    context={
        'user': request.user,
        'is_patient':data[0]["is_patient"],
        'is_doctor':data[0]["is_doctor"],
        'address':data[0]["address_line1"],
        'city':data[0]["city"],
        'state':data[0]["state"],
        'pincode':data[0]["pincode"],
        'img':data[0]["profile_picture"]
    }
    return render(request, 'dashboard.html',context)

def logout_view(request):
    logout(request)
    # Redirect to a success page, e.g., home page
    return redirect('dashboard')