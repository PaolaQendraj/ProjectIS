from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Vakte(models.Model):
    emri = models.CharField(max_length=20)

    def __str__(self):
        return self.emri

class Ushqimet(models.Model):
    emri = models.CharField(max_length=50)
    sasi = models.IntegerField()
    kalori = models.FloatField()
    proteina = models.FloatField()
    sheqerna = models.FloatField()
    yndyrna = models.FloatField()
    fibra = models.FloatField()
    sasi_total = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='media')
    vaktet = models.ForeignKey(Vakte, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.emri

class Pyetesor(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default='01')
    pesha = models.FloatField()
    gjatesia = models.FloatField()
    ditelindja = models.DateField(auto_now=False, auto_now_add=False,default='1998-01-01')
    qellimi = models.CharField(max_length=100, default='humbjepeshe')
    aktiv = models.CharField(max_length=100, default='humbjepeshe')
    lloji = models.CharField(max_length=100, default='humbjepeshe')
    gjinia = models.CharField(max_length=100, default='humbjepeshe')

    def __int__(self):
        return self.pesha
