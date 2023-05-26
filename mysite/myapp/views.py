from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
import pickle
from django.conf import settings


def home(request):
    if 'expensebtn' in request.POST:
        return redirect('expenses')

    if 'paymentbtn' in request.POST:
        return redirect('payments')

    if 'bankentry' in request.POST:
        return redirect('bankentry')

    if 'deliveryconfirmation' in request.POST:
        return redirect('deliveryconfirmation')

    return render(request, "home.html")

def expenses(request):
    return render(request, "expenses.html")

def payments(request):
    return render(request, "payments.html")

def bankentry(request):
    return render(request, "bankentry.html")

def deliveryconfirmation(request):
    return render(request, "deliveryconfirmation.html")

def postmessage(request):
    return render(request, "postmessage.html")

def loginpage(request):
    
    if request.method == "POST":
        passcode = request.POST.get("passcode")

        if passcode == "1234":
            return redirect("home")
        else:
            return render(request, "loginpage.html",context = {"mymessage":"Incorrect passcode.","Flag":"True"})            


    return render(request, "loginpage.html")
