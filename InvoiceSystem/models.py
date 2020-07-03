from django.db import models

# Create your models here.
class Invoices(models.Model):
    invoice_number= models.IntegerField(primary_key=True)
    user_id = models.CharField(max_length=100)
    vendor_name= models.CharField(max_length=100)
    invoice_date= models.DateField()
    pdf_copy = models.FileField(upload_to='pdfs/')
    

class ListOfItems(models.Model):
    user_id = models.CharField(max_length=100)
    item_description = models.CharField(max_length=1000)
    item_quantity = models.IntegerField()
    item_rate = models.FloatField()
    invoice_number = models.ForeignKey(Invoices,on_delete=models.CASCADE)
