from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,auth
from django.http import FileResponse, HttpResponseServerError
from django.shortcuts import render, redirect
import os
from .models import *


# Create your views here.
def profile(request):
    return render(request,"profile.html")

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        mail=request.POST['mail']
        password=request.POST['password']
        user=User()
        user.username=username
        user.email=mail
        user.set_password(password)
        user.save()

        return redirect('loginpage')
    return render(request,"register.html")

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            pass
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('home')


def home(request):
    return render(request,"index.html")

def features(request):
    return render(request,"features1.html")

def userpolicy(request):
    return render(request,"userpolicy.html")

def policy0(request):
    filepath=os.path.join('static','policy0.pdf')
    return FileResponse(open(filepath,'rb'),content_type='application/pdf')

def policy1(request):
    return render(request,"policy1.html")

def policy2(request):
    filepath = os.path.join('static', 'policy2.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

def policy3(request):
    filepath = os.path.join('static', 'policy3.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

def policy4(request):
    filepath = os.path.join('static', 'policy4.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

def policy5(request):
    filepath = os.path.join('static', 'policy5.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

def calculator(request):
    return render(request,"calculator.html")

def eduloan(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        street = request.POST['street']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        mail = request.POST['mail']
        dob = request.POST['dob']
        gender = request.POST['gender']
        reqamount = request.POST['reqamount']
        annualincome = request.POST['annualincome']
        eloan = EduLoan()
        eloan.fname = fname
        eloan.lname = lname
        eloan.street = street
        eloan.city = city
        eloan.state = state
        eloan.zipcode = zipcode
        eloan.mail = mail
        eloan.dob = dob
        eloan.gender = gender
        eloan.reqamount = reqamount
        eloan.annualincome = annualincome
        eloan.save()
        return redirect('smsg')
    return render(request, "eduloan.html")

def goldloan(request):
    if request.method =='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        street=request.POST['street']
        city=request.POST['city']
        state=request.POST['state']
        zipcode=request.POST['zipcode']
        mail=request.POST['mail']
        dob=request.POST['dob']
        gender=request.POST['gender']
        reqamount=request.POST['reqamount']
        annualincome=request.POST['annualincome']
        gloan=GoldLoan()
        gloan.fname=fname
        gloan.lname=lname
        gloan.street=street
        gloan.city=city
        gloan.state=state
        gloan.zipcode=zipcode
        gloan.mail=mail
        gloan.dob=dob
        gloan.gender=gender
        gloan.reqamount=reqamount
        gloan.annualincome=annualincome
        gloan.save()
        return redirect('smsg')
    return render(request,"goldloan.html")

def theme(request):
    return render(request,"theme.html")

def calculator(request):
    return render(request,"calculator.html")

def homeloan(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        street = request.POST['street']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        mail = request.POST['mail']
        dob = request.POST['dob']
        gender = request.POST['gender']
        reqamount = request.POST['reqamount']
        annualincome = request.POST['annualincome']
        hloan = HomeLoan()
        hloan.fname = fname
        hloan.lname = lname
        hloan.street = street
        hloan.city = city
        hloan.state = state
        hloan.zipcode = zipcode
        hloan.mail = mail
        hloan.dob = dob
        hloan.gender = gender
        hloan.reqamount = reqamount
        hloan.annualincome = annualincome
        hloan.save()
        return redirect('smsg')
    return render(request, "homeloan.html")

def personalloan(request):
    if request.method =='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        street=request.POST['street']
        city=request.POST['city']
        state=request.POST['state']
        zipcode=request.POST['zipcode']
        mail=request.POST['mail']
        dob=request.POST['dob']
        gender=request.POST['gender']
        reqamount=request.POST['reqamount']
        annualincome=request.POST['annualincome']
        ploan=PersonalLoan()
        ploan.fname=fname
        ploan.lname=lname
        ploan.street=street
        ploan.city=city
        ploan.state=state
        ploan.zipcode=zipcode
        ploan.mail=mail
        ploan.dob=dob
        ploan.gender=gender
        ploan.reqamount=reqamount
        ploan.annualincome=annualincome
        ploan.save()
        return redirect('smsg')
    return render(request,"personalloan.html")

def feedback(request):
    return render(request,"feedback.html")

def rights(request):
    filepath = os.path.join('static', 'rights.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

def tc(request):
    filepath = os.path.join('static', 't&c.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

def smsg(request):
    return render(request,"success_msg.html")

# def upload(request):
#     if request.method == 'POST':
#         customer = CustomerDocx(request.POST, request.FILES)
#         if customer.is_valid():
#             handle_uploaded_file(request.FILES['Aadhar'])
#             handle_uploaded_file(request.FILES['PAN'])
#             return redirect('smsg')
#     else:
#         customer = CustomerDocx()
#         return redirect('smsg')
#     return render(request,"upload.html",{'customer':customer})


def crypto(request):
    return render(request,"crypto.html")



