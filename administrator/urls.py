from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.admin_home, name='admin_home'),
    url(r'^member/tambah/$', views.admin_member_tambah, name='admin_member_tambah'),
    url(r'^member/edit/(?P<member_id>[0-9]+)/$', views.admin_member_edit, name='admin_member_edit'),
    url(r'^member/hapus/(?P<member_id>[0-9]+)/$', views.admin_member_hapus, name='admin_member_hapus'),
    url(r'^member/laporan/$', views.admin_member_laporan, name='admin_member_laporan'),
    url(r'^member/laporan/wilayah/$', views.admin_laporan_member_grafik, name='admin_laporan_member_grafik'),
]