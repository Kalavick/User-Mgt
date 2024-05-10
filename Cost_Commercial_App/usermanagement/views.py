#from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm


def home(request):
    return render(request, 'home.html', {})



# Create your views here.
@login_required
def register_view(request):
    if request.user.is_superuser:  # Only allow superusers to access the registration view
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'User registratoin successful. Please login')
                return redirect('login')  #redirect to login page after successful registration
        else:
            form = RegistrationForm()
        return render(request, 'register.html', {'form': form})
    else:
        return redirect('login')  # Redirect non-superusers to login page
    
#Explanation:

#We import the necessary modules: render, redirect, login_required, User, and RegistrationForm.
#We define the register_view function, which is responsible for rendering the registration form (register.html) and processing form submissions to create new user accounts.
#Inside the view function, we first check if the user accessing the registration page is a superuser. If not, they are redirected to the login page.
#If the user is a superuser, we check the request method. If it's a POST request, we initialize the registration form with the POST data and validate it. If the form is valid, we save the new user and redirect to the login page.
#If it's a GET request, we initialize an empty registration form and render the registration page (register.html) with the form.
    
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def password_reset_view(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(request=request)
            # Redirect to password reset done page
            messages.success(request, 'An email with password reset instructions has been sent.')
            return redirect('password_reset_done')
    else:
        form = PasswordResetForm()
    return render(request, 'password_reset.html', {'form': form})

#The output of this code would be:

#If a non-superuser attempts to access the register_view, they will be redirected to the login page.
#If a user submits the registration form with valid data, a new user will be created, and they will be redirected to the login page.
#If a user submits the login form with valid credentials, they will be redirected to the dashboard.
#If a user logs out, they will be redirected to the login page.
#If a user submits the password reset form with valid data, the password reset process will be initiated.
#There are a couple of missing pieces of functionality in the password_reset_view:
#After successfully resetting the password, it should redirect to a password reset done page.
#It should handle the case when the password reset form is submitted via GET, typically rendering a form to allow users to enter their email address to request a password reset email.

