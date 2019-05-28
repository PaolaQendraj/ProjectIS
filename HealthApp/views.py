from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *


# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request, 'html/index.html')

def register(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        if not User.objects.filter(email=email).exists():
            user = User.objects.create_user(email, username, password)

            user.username = username
            user.save()
            return render(request, 'html/healthapp_login.html')
        else:
            return render(request, 'html/healthapp_register.html')
    else:
        return render(request, 'html/healthapp_register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/pyetesori/')
            else:
                return HttpResponse('Your account is disabled')

        else:
            print('Invalid login details :{0},{1}'.format(username, password))
            return HttpResponseRedirect('/login/')

    else:
        return render(request, 'html/healthapp_login.html')



def pyetesori(request):
    if request.method == 'GET':
        return render(request, 'html/pyetesori.html')

def pyetesori_form(request):

    pesha = request.POST['pesha']
    gjatesia = request.POST['gjatesia']
    qellimi = request.POST['qellimi']
    aktiv = request.POST['aktiv']
    lloji = request.POST['lloji']
    gjinia = request.POST['gjinia']
    ditelindja = request.POST['ditelindja']

    pyetesori_info = Pyetesor(user=request.user, pesha=pesha, gjatesia=gjatesia, qellimi=qellimi, aktiv=aktiv, lloji=lloji, gjinia=gjinia, ditelindja=ditelindja)
    pyetesori_info.save()
    return render(request, 'html/index.html')

def planifikuesi_ushqimor(request):
    if request.method == 'GET':
        return render(request, 'html/planiushqimor.html')

def profili(request):
    if request.method == 'GET':
        return render(request, 'html/profili.html')


