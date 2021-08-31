from django.http.response import HttpResponse
from django.shortcuts import render
import requests, json
from datetime import datetime,date
# Create your views here.

def home(request):
    current_date = date.today()
    d = current_date.day
    m = current_date.month
    y = current_date.year
    pin = 123456
    if(request.method == 'POST'):
        pin = request.POST.get('pincode')
    url =""
    temp = pin
    if(len(str(temp))!=6):
        return HttpResponse("enter valid pin code")
    if(len(str(d))==1 and len(str(m))==1):
        d = int(d)
        m = int(m)
        url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date=0{}-0{}-{}".format(pin,d,m,y)
    if(len(str(d))==1):
        d = int(d)
        
        url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date=0{}-{}-{}".format(pin,d,m,y)
    if(len(str(m))==1):
        m = int(m)
        url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}-0{}-{}".format(pin,d,m,y)
    
    state = requests.get( url).json()
    state = state['sessions']
    context  = {"it": state}
    return render(request,"home.html",context)



def about(request):
    return render(request,'about.html')