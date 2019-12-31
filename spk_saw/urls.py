from django.conf.urls import url, include
from spk_saw import views

urlpatterns = [
	url(r'^$', views.Pengguna),
	url(r'^pengguna/$', views.PanelPengguna),
	url(r'^pengguna/akses/$', views.hakAksesView),
	url(r'^pengguna/pass/$', views.hakAksesViewUbah),
	url(r'^pengguna/ubah-password/$', views.hakAksesUbah),
	url(r'^pengguna/perusahaan/$', views.PerusahaanView),
	url(r'^pengguna/tambah-perusahaan/$', views.tambahPerusahaan),
	url(r'^pengguna/edit-perusahaan/(?P<id>[0-9]+)/$', views.editPerusahaan),
	url(r'^pengguna/hapus-perusahaan/(?P<id>[0-9]+)/$', views.deletePerusahaan),
	url(r'^pengguna/nilai/$', views.Menilai),
	# url(r'^member/akses/$', views.hakAksesView),
	# url(r'^member/pass/$', views.hakAksesViewUbah),
	# url(r'^member/ubah-password/$', views.hakAksesUbah),
	# url(r'^member/aturan/$', views.aturanView),
	# url(r'^member/konsul/', views.KonsultasiMember),
	# url(r'^member/edit/(?P<id>[0-9]+)/$', views.editMember),
]