# warga/api_urls.py
from django.urls import path, include
from .views import WargaListAPIView, WargaDetailAPIView, PengaduanListAPIView
#from .views import PengaduanViewSet, WargaViewSet
#from rest_framework.routers import DefaultRouter

# Buat sebuah router dan daftarkan ViewSet kita
#router = DefaultRouter()
#router.register(r'warga', WargaViewSet, basename='warga')
#router.register(r'aduan', PengaduanViewSet, basename='aduan')

urlpatterns = [
    path('warga/', WargaListAPIView.as_view(), name='api-warga-list'),
    path('warga/<int:pk>/', WargaDetailAPIView.as_view(), name='api-warga-detail'),
    path('aduan/<int:pk>/', PengaduanListAPIView.as_view(), name='api-pengaduan-list'),
    #path('', include(router.urls)),
]