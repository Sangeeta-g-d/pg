from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseForbidden,HttpResponseBadRequest
# Create your views here.


def index(request):
    return render(request,'index.html')


def registration(request):
    return render(request,'registration.html')


def login1(request):
    return render(request,'login.html')

def owner_register(request):
    if request.method == 'POST':
        pg_name = request.POST.get('name')
        email = request.POST.get('email')
        contact_number = request.POST.get('contact_number')
        address = request.POST.get('address')
        landmark = request.POST.get('landmark')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        if password != password:
            print("password is not matching")
            return render('owner_register')
        else:
            obj = NewUser.objects.create(first_name=pg_name,email=email,contact_number=contact_number,address=address,landmark=landmark,city=city,state=state,country=country,username=username,password=password)
            print("registration successful")
            return redirect('/')
    return render(request,'owner_register.html')