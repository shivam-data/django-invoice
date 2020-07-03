from InvoiceSystem.models import ListOfItems,Invoices
import datetime
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.db.models import Count



def calc():
    sum = 0
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)

    print(yesterday)
    try:
        records = Invoices.objects.get(invoice_date=yesterday)
        arr = ListOfItems.objects.filter(invoice_number = records)
        records_len = Invoices.objects.filter(invoice_date=yesterday)
        print(records)
        print(arr)
        for ite in arr:
            print(ite.item_rate)
            sum += ite.item_rate*ite.item_quantity
        return len(records_len),sum
    except:
        return 0,0

    

def sendmaildaily():
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    subject = 'Summary'
    invoices,total = calc()
    body = 'Dear {0}, here is summary for {1}.No. of invoices:{2},Total amount:{3}'.format('shivam',yesterday,invoices,total)
    myemail = 'www.princeshivam97@gmail.com'
    reciepent = 'shivam.160410107094@gmail.com'
    send_mail(subject,body,myemail,[reciepent],fail_silently=False)
