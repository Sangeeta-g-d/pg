from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseForbidden,HttpResponseBadRequest
from .models import NewUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
# Create your views here.


def index(request):
    return render(request,'index.html')


def registration(request):
    return render(request,'registration.html')




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
    alert_message = None  # Initialize alert message variable
    
    if request.method == 'POST':
       
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.user_type == 'Owner' and user.status:
                login(request, user)
                return redirect('/owner_dashboard')
            elif user.user_type == 'Owner' and not user.status:
                print("Please wait, your account needs to be verified.")
                alert_message = 'Please wait, your account needs to be verified.'
            else:
                alert_message = 'Invalid username or password.'
        else:
            alert_message = 'User not found.'  # Display "User not found" message here if the user is None.

    return render(request, 'login.html', {'alert_message': alert_message})

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        i = request.user.id
        print("idddddddddddddd",i)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('admin_db')
        elif user is not None and not user.is_superuser:
            messages.error(request, 'invalid user')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'admin_login.html')

def admin_db(request):
    return render(request,'admin_db.html')

def admin_logout(request):
    logout(request)
    # Redirect to a specific page after logout (optional)
    return redirect('/admin_login')

def pg_list(request):
    obj = NewUser.objects.filter(user_type='Owner')
    context = {
        'obj':obj,
    }
    return render(request,'pg_list.html',context)

def update_status(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        user_id = request.POST.get('user_id')
        user = get_object_or_404(NewUser, id=user_id)
        print("userrrrrrr",user)
        
        # Assuming 'status' is a BooleanField in your model
        user.status = True
        user.save()
        
        return JsonResponse({'message': 'Status updated successfully!'})
    return JsonResponse({}, status=400)

def owner_dashboard(request):
    return render(request,'owner_dashboard.html')