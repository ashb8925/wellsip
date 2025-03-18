from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .forms import RegisterForm
import random

from .models import UsersModel


# Create your views here.

def login_screen(request):
    print('user post', request.POST)
    if request.user.is_authenticated:
        return redirect('wellsip:home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print('email', email)
        print('password', password  )


        user = authenticate(request, email=email, password=password)
        if user is not None:
            print('user', user)
            login(request, user)
            print('login', user)
            return redirect('wellsip:home')
        else:
            print('not user found')
            messages.error(request, "Invalid username or password", extra_tags='error')

    return render(request, 'login_pages/login_screen.html')

def register_screen(request):
    if request.method == "POST":
        print('POST',request.POST)
        entered_otp = request.POST.get("otp")
        if "otp" in request.session:
            print('found stored otp')
            stored_otp = request.session.get("otp")
            print('found stored otp', stored_otp)
        else:
            return JsonResponse({'status':'failed', 'message': 'OTP expired !'})

        if stored_otp and str(entered_otp) == str(stored_otp):
            # Retrieve user data from session
            registration_data = request.session.get("registration_data")
            print('registration data', registration_data)

            if registration_data:
                User = get_user_model()  # Get the User model dynamically
                user = User.objects.create(
                    username=registration_data["email"],
                    first_name=registration_data["first_name"],
                    last_name=registration_data["last_name"],
                    email=registration_data["email"],
                    password=registration_data["hashed_password"],  # Already hashed
                )
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user)
                # Clear session data after successful registration
                request.session.flush()

                messages.success(request, "Registration successful! You can now log in.")
                return redirect("wellsip:home")
            else:
                return redirect('wellsip:register-screen')
        else:
            messages.error(request, "Incorrect OTP ! Try again.")
            return JsonResponse({'status': 'failed', 'message': 'Incorrect OTP, Try again!'})

    return render(request, 'login_pages/register_screen.html')

@require_http_methods(['POST'])
def store_registration_data(request):
    print('POST', request.POST)
    form = RegisterForm(request.POST)
    if form.is_valid():
        # Extract cleaned data
        full_name = form.cleaned_data["full_name"]
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        first_name = full_name['first_name']
        last_name = full_name['last_name']

        if UsersModel.objects.filter(email=email).exists():
            return JsonResponse({
                'status': 'failed',
                'message': 'Email already Exists !'
            })

        # Generate OTP
        otp = random.randint(100000, 999999)
        print(otp)
        # Store validated data in session
        request.session["registration_data"] = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "hashed_password": make_password(password),  # Hash before storing
        }
        request.session["otp"] = otp
        request.session.set_expiry(300)

        # Send OTP to user's email
        send_mail(
            "Your OTP Code",
            f"Your OTP for registration is {otp}. It is valid for 5 minutes.",
            "sunnyash53@gmail.com",  # Replace with actual sender email
            [email],
            fail_silently=False,
        )
        return JsonResponse({
            'status': 'success',
            'message': 'verify otp'
        })
    else:
        errors = {field: error.get_json_data() for field, error in form.errors.items()}
        return JsonResponse({
            'status': 'failed',
            'message': 'Validation failed !',
            'errors': errors
        })

# Resend OTP API
@csrf_exempt
@require_http_methods(['POST'])
def resend_otp(request):
    # Check if OTP and email are available in the session
    if "otp" in request.session and "registration_data" in request.session:
        email = request.session["registration_data"]["email"]
        otp = request.session["otp"]
        if not "otp_attempt" in request.session:
            request.session["otp_attempt"] = 2
        else:
            if request.session["otp_attempt"] < 4:
                request.session["otp_attempt"] += 1
            else:
                print('blocking otp', request.session["otp_attempt"])
                return JsonResponse({
                    'status': 'failed',
                    'message': 'block otp'
                })
        request.session.set_expiry(300)
        # Send the OTP to the user's email again
        send_mail(
            "Your OTP Code - Resent",
            f"Your OTP for registration is {otp}. It is valid for 5 minutes.",
            "sunnyash53@gmail.com",  # Replace with actual sender email
            [email],
            fail_silently=False,
        )

        return JsonResponse({
            'status': 'success',
            'message': 'OTP resent successfully.'
        })
    else:
        return JsonResponse({
            'status': 'failed',
            'message': 'OTP Expired !'
        })

def forgot_password(request):
    return render(request, 'login_pages/forgot_password.html')

def home_screen(request):
    return render(request, 'home1.html')

def test(request):
    return render(request, 'test2.html')
