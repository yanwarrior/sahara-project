from django.db import models
from django.contrib.auth.models import User


class Paket(models.Model):
    nama = models.CharField(max_length=30)
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

class Member(User):
    paket = models.ForeignKey(Paket)
    pembayaran =  models.ForeignKey(Pembayaran)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = "Data Member"
