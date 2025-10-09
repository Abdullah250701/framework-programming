from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Warga, Pengaduan
from .forms import WargaForm, PengaduanForm  # tambahkan 

# View untuk daftar warga
class WargaListView(ListView):
    model = Warga

# View untuk daftar pengaduan
class PengaduanListView(ListView):  
    model = Pengaduan
    template_name = 'warga/pengaduan_list.html'

#  View baru untuk tambah warga
class WargaCreateView(CreateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga_list')  # kembali ke daftar warga setelah sukses

    # View baru untuk tambah pengaduan
class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan_list')  # kembali ke daftar pengaduan
