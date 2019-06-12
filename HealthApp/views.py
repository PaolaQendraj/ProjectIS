from datetime import date

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
                return HttpResponseRedirect('/index/')
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
        mengjes = Mengjesi.objects.all()
        dreke = Dreka.objects.all()
        darke = Darka.objects.all()
        snack = Snacks.objects.all()
        informacion = Pyetesor.objects.filter(user=request.user)
        BMI = 0.0
        IBW = 0.0
        body_fat = 0.0
        uji = 0.0
        koeficienti = 0.0
        aktivitet = 0.0
        kalori_ditore = 0.0
        today = date.today()
        for pr in informacion:
            BMI = round(pr.pesha / (pr.gjatesia / 100) ** 2, 2)
            IBW = round(22 * ((pr.gjatesia / 100) ** 2), 2)
            mosha = today.year - pr.ditelindja.year
            uji = round(pr.pesha * 0.033, 2)
            if pr.gjinia == 'femer':
                if mosha < 18:
                    body_fat = round(1.51 * BMI - 0.70 * mosha + 1.4, 2)
                else:
                    body_fat = round(1.20 * BMI + 0.23 * mosha - 5.4, 2)
            else:
                if mosha < 18:
                    body_fat = round(1.51 * BMI - 0.70 * mosha - 2.2, 2)
                else:
                    body_fat = round(1.20 * BMI + 0.23 * mosha - 16.2, 2)

            if pr.gjinia == 'femer':
                if body_fat <= 18:
                    koeficienti = 1.0
                elif body_fat >= 19 and body_fat <= 28:
                    koeficienti = 0.95
                elif body_fat >= 29 and body_fat <= 38:
                    koeficienti = 0.90
                elif body_fat > 38:
                    koeficienti = 0.85
            else:
                if body_fat <= 14:
                    koeficienti = 1.0
                elif body_fat >= 15 and body_fat <= 20:
                    koeficienti = 0.95
                elif body_fat >= 21 and body_fat <= 28:
                    koeficienti = 0.90
                elif body_fat > 28:
                    koeficienti = 0.85

            if pr.aktiv == 'aspak':
                aktivitet = 1.55
            elif pr.aktiv == 'pakaktiv':
                aktivitet = 1.65
            else:
                aktivitet = 1.85

            if pr.gjinia == 'femer':
                kalori_ditore = round(pr.pesha * 0.9 * 24 * koeficienti * aktivitet, 2)
            else:
                kalori_ditore = round(pr.pesha * 1 * 24 * koeficienti * aktivitet, 2)
        return render(request, 'html/planiushqimor.html', {'mengjesi': mengjes, 'dreka':dreke, 'darka':darke, 'snacks':snack,'infoprofili': informacion,'BMI': BMI, 'IBW':IBW, 'mosha': mosha, 'body_fat':body_fat, 'uji':uji, 'kalori_ditore': kalori_ditore})


def profili(request):
    if request.method == 'GET':
        informacion = Pyetesor.objects.filter(user=request.user)
        BMI = 0.0
        IBW = 0.0
        body_fat = 0.0
        uji = 0.0
        koeficienti = 0.0
        aktivitet = 0.0
        kalori_ditore = 0.0
        today = date.today()
        for pr in informacion:
            BMI = round(pr.pesha / (pr.gjatesia/100) ** 2, 2)
            IBW = round(22 * ((pr.gjatesia/100)**2), 2)
            mosha = today.year - pr.ditelindja.year
            uji = round(pr.pesha * 0.033, 2)
            if pr.gjinia == 'femer':
                if mosha < 18:
                    body_fat = round(1.51 * BMI - 0.70 * mosha + 1.4, 2)
                else:
                    body_fat = round(1.20 * BMI + 0.23 * mosha - 5.4, 2)
            else:
                if mosha < 18:
                    body_fat = round(1.51 * BMI - 0.70 * mosha - 2.2, 2)
                else:
                    body_fat = round(1.20 * BMI + 0.23 * mosha - 16.2, 2)

            if pr.gjinia == 'femer':
                if body_fat <=18:
                    koeficienti = 1.0
                elif body_fat >= 19 and body_fat <= 28:
                    koeficienti = 0.95
                elif body_fat >= 29 and body_fat <=38:
                    koeficienti = 0.90
                elif body_fat > 38:
                    koeficienti = 0.85
            else:
                if body_fat <=14:
                    koeficienti = 1.0
                elif body_fat >= 15 and body_fat <= 20:
                    koeficienti = 0.95
                elif body_fat >=21 and body_fat <= 28:
                    koeficienti = 0.90
                elif body_fat > 28:
                    koeficienti = 0.85

            if pr.aktiv == 'aspak':
                aktivitet = 1.55
            elif pr.aktiv == 'pakaktiv':
                aktivitet = 1.65
            else:
                aktivitet = 1.85

            if pr.gjinia == 'femer':
                kalori_ditore = round(pr.pesha * 0.9 * 24 * koeficienti * aktivitet, 2)
            else:
                kalori_ditore = round(pr.pesha * 1 * 24 * koeficienti * aktivitet, 2)

        return render(request, 'html/profili.html', {'infoprofili': informacion,'BMI': BMI, 'IBW':IBW, 'mosha': mosha, 'body_fat':body_fat, 'uji':uji, 'kalori_ditore': kalori_ditore})


def aktiviteti_fizik(request):
    if request.method == 'GET':
        natyre = Sport_Natyre.objects.all()
        ujor = Sport_Ujore.objects.all()
        grup = Sport_Grupe.objects.all()
        palester = Sport_Palester.objects.all()
        informacion = Pyetesor.objects.filter(user=request.user)
        for info in informacion:
            pesha = info.pesha
        return render(request, 'html/aktiviteti_fizik.html',{'sportnatyre': natyre, 'sportujor': ujor, 'sportgrupi': grup, 'sportpalester': palester,'informacion': informacion, 'pesha': pesha})

