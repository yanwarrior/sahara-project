from django.db import models
from django.contrib.auth.models import User


class Paket(models.Model):
    nama = models.CharField(max_length=30)
    keterangan = models.TextField()
    status = models.BooleanField()
    harga = models.IntegerField()

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name = "pizza"
        verbose_name_plural = "Master Paket"


class Pembayaran(models.Model):
    jenis = models.CharField(max_length=30)

    def __str__(self):
        return self.jenis

    class Meta:
        verbose_name_plural = "Master Pembayaran"

class Wilayah(models.Model):
    nama = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nama

class Member(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.TextField()
    wilayah = models.ForeignKey(Wilayah)
    paket = models.ForeignKey(Paket)
    pembayaran =  models.ForeignKey(Pembayaran)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = "Data Member"
