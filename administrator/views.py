from django.shortcuts import render
from django.http import HttpResponse
from .helpers.grafik_chart import chart_member

from registrasi.models import Member

def admin_home(request):
    """
    Home Admin.

    template : member_list.html
    model    : Member
    """
    return render(request, 'base_site.html', {})
    #    return HttpResponse("Halaman Home")

def admin_member_tambah(request):
    """
    Tambah member.

    template : member_crud.html
    model    : Member
    form     : ModelMemberTambahForm
    """
    # GOTO ADD FORM
    return HttpResponse("Halaman admin member tambah (form)")

def admin_member_edit(request, member_id):
    """
    Edit data member.

    template : member_crud.html
    model    : Member
    form     : ModelMemberEditForm
    """
    # GOTO ADD FORM
    return HttpResponse("Halaman admin member edit dengan id ({})".format(member_id))


def admin_member_hapus(request, member_id):
    """
    Hapus data member.

    template : member_crud.html
    model    : Member
    form     : ModelMemberHapusForm
    """
    return HttpResponse("Halaman hapus member dengan id ({})".format(member_id))


def admin_member_laporan(request):
    """
    Laporan calon member.

    view untuk menampilkan calon member dari status aktif
    atau tidak aktifnya.
    """
    return HttpResponse("Halaman laporan member dengan status aktif dan tidak aktif")

def admin_laporan_member_grafik(request):
    """
    Laporan member dengan grafik.

    view untuk menampilkan data member dengan grafik pygal
    dengan wilayah.
    """
    context = {
        'grafik': chart_member(),
    }
    return render(request, 'administrator/admin_laporan_member_grafik.html', context)

def admin_laporan_produk(request):
    """
    Laporan produk.
    """
    pass