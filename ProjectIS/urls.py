"""ProjectIS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from HealthApp.views import *
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('register/', register),
    path('register_pass/', register_pass),
    path('register_exist/', register_exist),
    path('login_none/', login_none),
    path('login/', login_user),
    path('login_success/', login_success),
    path('register_success/',register_success),
    path('pyetesori/', pyetesori),
    path('planifikuesi_ushqimor/', planifikuesi_ushqimor),
    path('aktiviteti_fizik/', aktiviteti_fizik),
    path('monitorues_uji/', monitorues_uji),
    path('profili/', profili),
    path('pyetesori_form/', pyetesori_form),
    path('accounts/', include('django.contrib.auth.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

