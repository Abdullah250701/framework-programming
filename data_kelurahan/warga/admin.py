from django.contrib import admin
from .models import Warga, Pengaduan  # tambahkan Pengaduan

# Daftarkan model agar muncul di halaman admin
admin.site.register(Warga)
admin.site.register(Pengaduan)
