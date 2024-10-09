from django.contrib.auth.models import User,auth
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserRegisterForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Retrieve the user by email
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'User with this email does not exist.')
            return redirect('login')

        # Authenticate using the username (Django uses username by default)
        user = auth.authenticate(username=user.username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid password')
            return redirect('login')

    return render(request, 'login.html')




def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        # password2 = request.POST['password2']

        if User.objects.filter(username=username).exists():
        	messages.info(request, 'Username Taken')
        	return redirect('register')
        elif User.objects.filter(email=email).exists():
        	messages.info(request, 'Email Taken')
        	return redirect('register')
        else:
        	user = User.objects.create_user(username=username, password=password, email=email,first_name=first_name)
        	user.save();
        	print("User created")
        	return redirect('login')

    else:
        return render(request, 'register.html')