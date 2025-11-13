from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Warga, Pengaduan
from .forms import WargaForm, PengaduanForm
# Impor baru untuk DRF
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import WargaSerializer, PengaduanSerializer

# ... (class view yang sudah ada untuk HTML) ...

# --- API VIEWS ---
class WargaListAPIView(ListAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer

class WargaDetailAPIView(RetrieveAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer

class PengaduanListAPIView(ListAPIView):
    queryset = Pengaduan.objects.all()
    serializer_class = PengaduanSerializer


# Daftar warga
class WargaListView(ListView):
    model = Warga
    template_name = 'warga/warga_list.html'

# Detail warga 
class WargaDetailView(DetailView):
    model = Warga
    template_name = 'warga/warga_detail.html'

# Tambah warga 
class WargaCreateView(CreateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga_list')

# Edit warga 
class WargaUpdateView(UpdateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga_list')

# Hapus warga
class WargaDeleteView(DeleteView):
    model = Warga
    template_name = 'warga/warga_confirm_delete.html'
    success_url = reverse_lazy('warga_list')

# Daftar pengaduan 
class PengaduanListView(ListView):
    model = Pengaduan
    template_name = 'warga/pengaduan_list.html'

# Tambah pengaduan 
class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan_list')

# Edit pengaduan 
class PengaduanUpdateView(UpdateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan_list')

# Hapus pengaduan 
class PengaduanDeleteView(DeleteView):
    model = Pengaduan
    template_name = 'warga/pengaduan_confirm_delete.html'
    success_url = reverse_lazy('pengaduan_list')
