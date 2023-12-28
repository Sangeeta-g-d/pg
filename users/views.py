from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseForbidden,HttpResponseBadRequest
from .models import NewUser
from django.contrib.auth.hashers import make_password
# Create your views here.


def index(request):
    return render(request,'index.html')

def owner_register(request):
    if request.method == 'POST':
        pg_name = request.POST.get('name')
        email = request.POST.get('email')
        contact_number = request.POST.get('contact_number')
        address = request.POST.get('address')
        landmark = request.POST.get('landmark')
        area = request.POST.get('area')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(password)
        password1 = request.POST.get('password1')
        print(password1)
        user_type = request.POST.get('user_type')
        if password == password1:
            passw = make_password(password)
            obj = NewUser.objects.create(first_name=pg_name,email=email,contact_number=contact_number,address=address,landmark=landmark,city=city,state=state,country=country,username=username,password=passw,user_type=user_type)
            print("registration successful")
            return redirect('/')
            
        else:
            print("password is not matching")
            return redirect('owner_register')
    return render(request,'owner_register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.user_type == 'student' and user.payment_status:
                login(request, user)
                return redirect('dashboard', user.id)
            elif user.user_type == 'student' and not user.payment_status:
                messages.error(request, 'Please wait, your account needs to be verified.')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'User not found.')  # Display "User not found" message here if the user is None.

    return render(request, 'login.html')