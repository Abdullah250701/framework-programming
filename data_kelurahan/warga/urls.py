from django.urls import path
from .views import ( WargaListView, PengaduanListView, WargaCreateView, PengaduanCreateView )

urlpatterns = [
    path('', WargaListView.as_view(), name='warga_list'),
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan_list'),
    path('tambah/', WargaCreateView.as_view(), name='warga_tambah'),  # URL untuk form tambah warga
    path('pengaduan/tambah/', PengaduanCreateView.as_view(), name='pengaduan-tambah'),
]
