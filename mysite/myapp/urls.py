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
]