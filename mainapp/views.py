from django.shortcuts import render, redirect
from django.contrib import messages
from .models import new_passwordsModel
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login

# Create your views here.
def home(request):
    return render(request, 'index.html')

def logout(request):
    # logout(request)
    return redirect('/')

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

            all_users = User.objects.all()
            count_users = all_users.count()
            context= {'count_users': str(count_users), 'all_users': all_users}
            # messages.success(request, 'Sign up successful...')
            return redirect('dashboard', context)

# handles logging in a user
def log_in(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass']

        user = authenticate(
            request,
            username = email,
            password = password
        )

        if user is not None:
            login(request,user)

            all_users = new_passwordsModel.objects.all()
            count_users = all_users.count()
            context= {'count_users': str(count_users), 'all_users': all_users}
            print('logs user in')
            return redirect('dashboard')
            return render(request, 'dashboard.html', context)

        else:
            print('/cant find you')
            # pass
            # messages.warning(request, 'Your Credentials do not match our records, pls try again!')
            return redirect('loggedin')

        all_users = new_passwordsModel.objects.all()
        count_users = all_users.count()
        context= {'count_users': str(count_users), 'all_users': all_users}
        return render(request, 'dashboard.html', context)

    else: 
        return redirect('/')

@login_required(redirect_field_name='loggedin')
def dashboard(request):
    all_users = new_passwordsModel.objects.all()
    count_users = all_users.count()
    context= {'count_users': str(count_users), 'all_users': all_users}
    print('redirects user')
    # return redirect('dashboard')
    return render(request, 'dashboard.html', context)
    # return render(request, 'dashboard.html')

def new_password(request):
    if request.method == 'POST':
        website = request.POST['website']
        password = request.POST['password']
        username = request.POST['username']
        user_mail = request.POST['user_mail']

        # store credentials
        new_passwordsModel.objects.create(
            website = website,
            username = username,
            user_email = user_mail,
            password = password,
        )

        return redirect('dashboard')

