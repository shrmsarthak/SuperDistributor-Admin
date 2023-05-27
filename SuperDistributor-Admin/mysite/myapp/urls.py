from django.urls import path

from . import views

urlpatterns = [
    path('', views.loginpage, name='loginpage'),
    path('home/', views.home, name='home'),
    path('expenses/', views.expenses, name='expenses'),
    path('payments/', views.payments, name='payments'),
    path('bankentry/', views.bankentry, name='bankentry'),
    path('deliveryconfirmation/', views.deliveryconfirmation, name='deliveryconfirmation'),
    path('postmessage/', views.postmessage, name='postmessage'),
    path('adddealer/', views.adddealer, name='adddealer'),
    path('addemployee/', views.addemployee, name='addemployee'),
    path('salevoucher/', views.salevoucher, name='salevoucher'),
    path('purchase/', views.purchase, name='purchase'),
    path('vehicletracking/', views.vehicletracking, name='vehicletracking'),
    path('inward/', views.inward, name='inward'),
    path('outward/', views.outward, name='outward'),
    path('postcomplaint/', views.postcomplaint, name='postcomplaint'),
    path('claimdataentry/', views.claimdataentry, name='claimdataentry'),
    
]