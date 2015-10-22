from django import forms
from registrasi.models import Wilayah
from registrasi.models import Pembayaran
from registrasi.models import Paket

def wilayah_choices():
    return [(o.id, str(o)) for o in Wilayah.objects.all()]

def pembayaran_choices():
    return [(o.id, str(o.jenis)) for o in Pembayaran.objects.all()]

def gender_choices():
    return (('P', 'Pria',), ('W', 'Wanita',))

def paket_choices():
    return [(o.id, str(o.nama) + " " + str(o.harga)) for o in Paket.objects.all()]

class FormRegistrasi(forms.Form):
    nomer = forms.CharField(max_length=5,label='Nomer Urut', widget=forms.TextInput(attrs={'class':'form-control'}))
    nama = forms.CharField(max_length=30, label='Nama', widget=forms.TextInput(attrs={'class':'form-control'}))
    alamat = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    wilayah = forms.ChoiceField(choices=wilayah_choices(), widget=forms.Select(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
    handphone = forms.CharField(label='Nomer Handphone', max_length=16, widget=forms.TextInput(attrs={'class':'form-control'}))
    tempat_lahir = forms.CharField(label='Tempat Lahir', max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
    tanggal_lahir = forms.CharField(label='Tanggal Lahir', widget=forms.DateInput(attrs={'class':'form-control'}))
    pembayaran = forms.ChoiceField(choices=pembayaran_choices(), widget=forms.Select(attrs={'class':'form-control'}))
    jenis_kelamin = forms.ChoiceField(choices=gender_choices(), widget=forms.RadioSelect(attrs={'class':'form-control'}))
    paket_sahara = forms.ChoiceField(choices=paket_choices(), widget=forms.Select(attrs={'class':'form-control'}))




