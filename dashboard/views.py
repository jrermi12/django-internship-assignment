from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
        except KeyError:
            messages.error(request, 'Please provide both username and password.')
            return render(request, 'userAuth/login.html')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'userAuth/login.html')