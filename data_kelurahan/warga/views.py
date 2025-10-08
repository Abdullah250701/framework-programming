from django.views.generic import ListView
from .models import Warga, Pengaduan

class WargaListView(ListView):
    model = Warga

class PengaduanListView(ListView):  
    model = Pengaduan
    template_name = 'warga/pengaduan_list.html'
