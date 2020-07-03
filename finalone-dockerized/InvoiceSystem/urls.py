from django.urls import path

from . import views

urlpatterns = [
    path('pdfupload',views.upload,name='pdfupload'),
    path('addinvoice',views.addinvoice,name='addinvoice'),
    path('disp/<int:id>',views.disp,name='disp'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('manager',views.manager,name='manager'),
    path('viewmanager/<slug:id>',views.viewmanager,name='viewmanager'),
    path('managerdisp/<int:id>',views.dispmanager,name='dispmananger'),
    ]
