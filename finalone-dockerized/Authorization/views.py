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
                user = User.objects.create_user(username=username,password=password1,email=email)
                user.save()
                messages.success(req,'User Created')
                auth.login(req,user)
                return redirect('/invoice/pdfupload')
            else:
                return 
        else:
            return redirect('/register')
    return render(req,'register.html')

def login(req):
    print(get_current_site(req))
    print('in login part')
    if req.method == 'POST':
        print('In the login')
        username = req.POST['username']
        password = req.POST['password']

        user = auth.authenticate(username = username,password= password)

        if user is not None:
            auth.login(req,user)
            return redirect('/invoice/pdfupload')
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