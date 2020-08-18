from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def register_new_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['full_name']
        password = request.POST['password']

        # if user exists 
        if User.objects.filter(email=email).exists():
            print ('Already exists')
            messages.warning(request, 'User with '+ email +' already exists')
            return redirect('signup')

        else:
            messages.success(request, 'Sign up in progress...')
            user = User.objects.create_user(
                first_name = name,
                password = password,
                username = email,
                email = email,
            )

            user.save()
            # messages.success(request, 'Sign up successful...')
            return redirect('signup')