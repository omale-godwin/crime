from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
import random
from .models import Evident, Report, Weakness
# Create your views here.
def report(request):

    if  request.method == 'POST':  
        name = request.POST['name']
        regnumber = request.POST['regnumber']
        title = request.POST['title']
        dats = request.POST['date']
        emergency = request.POST['emergency']
        email = request.POST['email']
        phone = request.POST['phone']
        description = request.POST['description']
        casetype = request.POST['casetype']
        data = Report(name=name, regnumber=regnumber, title=title, dats=dats, emergency=emergency, email=email,
        phone=phone, description=description, casetype=casetype)
        data.save()
        
        idn = data.objects.get(email)
        if idn != '':
            return redirect('login')
        print(idn)
        request.session['name'] = name
        request.session['regnumber'] = regnumber
        request.session['emergency'] = emergency
        request.session['email'] = email
        request.session['phone'] = phone
        request.session['casetype'] = casetype
        request.session['title'] = title
        request.session['dats'] = dats
        request.session['description'] = description

             
        
        return redirect('evident')
  
  
    return render(request, 'report/report.html')


def evident(request):

    if request.method == 'POST' and request.FILES['myevident']:
         photo_main = request.FILES['myevident']
         dats = request.POST['dates']
     
         user_id = User.objects.get(id=request.user)

         evident_data = Evident(photo_main=photo_main, dates=dats, user_id=user_id)
         evident_data.save()
         
         messages.success(request, 'Evident sucessfuly')
         return redirect('weakness')
    else:
        redirect('evident')


    return render(request, 'report/evident.html')

def weakness(request):
    if request.method == 'POST':  
        w_name = request.POST['name']
        w_regnumber = request.POST['regnumber']
        w_dats = request.POST['date']
        w_email = request.POST['email']
        w_phone = request.POST['phone']
        w_description = request.POST['description']
        user_id = User.objects.get(id=request.user.id)
      
       
        

        data_weakness = Weakness(user_id=user_id, name=w_name, regnumber=w_regnumber, dats=w_dats, email=w_email, phone=w_phone, description=w_description)
        data_weakness.save()
        
        
        

       
        return redirect('thank')
       
    return render(request, 'report/weakness.html')


def thank(request):
    return render(request, 'report/thank.html')


def dashboard(request):
    return render(request, 'report/dashboard.html')