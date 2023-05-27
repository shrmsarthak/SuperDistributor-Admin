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

    if 'salevoucher' in request.POST:
        return redirect('salevoucher')

    if 'purchase' in request.POST:
        return redirect('purchase')

    if 'vehicletracking' in request.POST:
        return redirect('vehicletracking')

    if 'inward' in request.POST:
        return redirect('inward')

    if 'outward' in request.POST:
        return redirect('outward')

    if 'postcomplaint' in request.POST:
        return redirect('postcomplaint')

    if 'claimdataentry' in request.POST:
        return redirect('claimdataentry')

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

def adddealer(request):
    return render(request, "adddealer.html")

def addemployee(request):
    return render(request, "addemployee.html")

def salevoucher(request):
    return render(request, "salesvoucher.html")

def purchase(request):
    return render(request, "purchase.html")

def vehicletracking(request):
    return render(request, "vehicletracking.html")

def inward(request):
    return render(request, "inward.html")

def outward(request):
    return render(request, "outward.html")

def postcomplaint(request):
    return render(request, "postcomplaint.html")

def claimdataentry(request):
    return render(request, "claimdataentry.html")

def loginpage(request):
    
    if request.method == "POST":
        passcode = request.POST.get("passcode")

        if passcode == "1234":
            return redirect("home")
        else:
            return render(request, "loginpage.html",context = {"mymessage":"Incorrect passcode.","Flag":"True"})            


    return render(request, "loginpage.html")
