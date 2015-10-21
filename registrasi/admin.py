from django.contrib import admin
from .models import Paket, Pembayaran, Member


class AdminPaket(admin.ModelAdmin):
    pass

class AdminPembayaran(admin.ModelAdmin):
    pass

class AdminMember(admin.ModelAdmin):
    pass

admin.site.register(Paket, AdminPaket)
admin.site.register(Pembayaran, AdminPembayaran)
admin.site.register(Member, AdminMember)

