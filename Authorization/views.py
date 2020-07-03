from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site

# Create your views here.

def register(req):
    # username is remaining
    # password matching
    if req.method == 'POST':
        username = req.POST['username']
        email = req.POST['email']
        password1 = req.POST['password1']
        password2 = req.POST['password2']

        if password1:
            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    print('user')
                    messages.info(req,'User Already exists')
                    return render(req,'register.html')
                elif User.objects.filter(email=email).exists():
                    messages.info(req,'Email Already taken')
                    return render(req,'register.html')
                user = User.objects.create_user(username=username,password=password1,email=email)
                user.save()
                auth.login(req,user)
                return redirect('/invoice/pdfupload')
            else:
                messages.info(req,'Password not matching') 
                return render(req,'register.html')
        else:
            return redirect('/register')
    return render(req,'register.html')

def login(req):
    if req.method == 'POST':
        print('In the login')
        username = str(req.POST['username'])
        password = str(req.POST['password'])

        print(username,password)
        user = auth.authenticate(username = username,password= password)

        if user is not None:
            auth.login(req,user)
            return redirect('/invoice/pdfupload')
        else:
            messages.info(req,'Login Failed')
    return render(req,'login.html')

@login_required(login_url='/')
def logic(req):
    # the agent reference id -- req.user.id
    print(req.user.id)
    return HttpResponse('<h1>Logic part')

@login_required(login_url='/')
def logout(req):
    # on click of logout button
    auth.logout(req)
    if not req.user.is_authenticated:
        print('Not logged in')
    return redirect('/')