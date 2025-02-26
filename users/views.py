from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return render(request, 'users/register.html', {'error': 'Passwords do not match'})

        # ✅ Check if username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'users/register.html', {'error': 'Username already taken. Please choose another one.'})

        # ✅ Check if email already exists (optional)
        if User.objects.filter(email=email).exists():
            return render(request, 'users/register.html', {'error': 'Email already registered. Try logging in.'})

        # ✅ Create user with hashed password
        myuser = User.objects.create_user(username=username, email=email, password=password)
        myuser.save()

        return redirect('user_login')  # Redirect to login page

    return render(request, 'users/register.html')


def user_login(request):  # ✅ Renamed function
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            auth_login(request, user)  # ✅ Using Django's login function correctly
            return redirect('home')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid credentials'})

    return render(request, 'users/login.html')


def user_logout(request):
    auth_logout(request)  # ✅ Logs out the user
    return redirect('user_login')  # Redirects to login page after logout
