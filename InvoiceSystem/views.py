from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import Invoices,ListOfItems
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
import datetime
from django.contrib import messages
# Create your views here.
link = ''
token = ''

def sendmail(request,token,mail):
    subject = 'An agent Just added new invoice.Link For access Token'
    body =str(get_current_site(request))+'/invoice/viewmanager/'+str(token)
    myemail = 'www.princeshivam97@gmail.com'
    reciepent = str(mail)
    send_mail(subject,body,myemail,[reciepent],fail_silently=False)


@login_required(login_url='/login')
def addinvoice(req):
    print(req)
    userid = req.user.id
    if req.method == 'POST':
        print(userid)
        invoice_number = req.POST.get('InvoiceNumber')
        vendor_name = req.POST.get('VendorName')
        invoice_date = req.POST.get('InvoiceDate')
        global link
        global token
        #uf = req.FILES['pdf']
        #fs = FileSystemStorage()
        #name = fs.save(uf.name,uf)

        item_description = req.POST.get('item_d')
        item_quantity = req.POST.get('item_q')
        item_rate = req.POST.get('item_r')

        manager_mail = req.POST.get('manager_id')

        print(item_description)

        user = Invoices(invoice_number=invoice_number,user_id=userid,vendor_name=vendor_name,invoice_date=invoice_date,pdf_copy='123')
        user.save()

        token = get_random_string(length=16)
        sendmail(req,token,manager_mail)

        # print('Send mail!!')
        # subject = 'Hello Gandu'
        # body = '<h1>Dekh gandu automated message</h1>'
        # myemail = 'www.princeshivam97@gmail.com'
        # reciepent = 'meet2579@yahoo.com'
        # send_mail(subject,body,myemail,[reciepent],fail_silently=False)

        items = ListOfItems(invoice_number=user,item_description=item_description,item_quantity=item_quantity,item_rate=item_rate,user_id=userid)
        print(items)
        items.save()


        #context['url'] = fs.url(name)
        records = Invoices.objects.filter(user_id=userid)
        return render(req,'addinvoice.html',{'records':records,'link':link})
        #return redirect('/invoice/addinvoice')
    else:
        records = Invoices.objects.filter(user_id=userid)
        return render(req,'addinvoice.html',{'records':records,'link':link})

# def addinvoice(req,path):
#     return render(req,'addinvoice.html',path)
@login_required(login_url='/login')
def upload(req):
    userid = req.user.id
    if req.method == 'POST':
        print('post')
        filename = req.FILES['mypdf']
        if filename.size > 2097152 :
            messages.error(req,'File above limit')
            return render(req,'hello.htm')
        print(filename.size)
        fs = FileSystemStorage()
        name = fs.save(filename.name,filename)

        global link
        link = fs.url(name)
        
        records = Invoices.objects.filter(user_id=userid)
        return render(req,'addinvoice.html',{'link':link,'records':records})
    else:
        return render(req,'hello.htm')

@login_required(login_url='/login')    
def disp(req,id):
    userid = req.user.id
    arr =  ListOfItems.objects.filter(invoice_number = id,user_id=userid)
    return render(req,'invoice.html',{'records':arr})

@login_required(login_url='/login')
def delete(req,id):
    userid = req.user.id
    Invoices.objects.filter(invoice_number = id).delete()
    records = Invoices.objects.filter(user_id=userid)
    return render(req,'addinvoice.html',{'link':link,'records':records})


def viewmanager(req,id):
    #print(req.query.token)
    global token
    if str(id) == str(token): 
        records = Invoices.objects.all()
        return render(req,'manager.html',{'records':records})
    else:
        return HttpResponse('<h1>Access not allowed')

    
def dispmanager(req,id):
    print(id)
    userid = req.user.id
    arr = ListOfItems.objects.filter(invoice_number = id,user_id = userid)
    return render(req,'invoice-manager.html',{'records':arr})


