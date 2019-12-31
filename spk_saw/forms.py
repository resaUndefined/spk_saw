from django import forms
# from django.contrib.auth.models import User
from spk_saw.models import Perusahaan


# class PenilaianForm(forms.ModelForm):
# 	class Meta:
# 		model = Nilai
# 		fields = (
# 			'hotel',
# 			'c1',
# 			'c2',
# 			'c3',
# 			'c4',
# 			)


# class NilaiForm(forms.Form):
# 	hotel = forms.CharField()
# 	c1 = forms.CharField()
# 	c2 = forms.CharField()
# 	c3 = forms.CharField()
# 	c4 = forms.CharField()
class tambahPerusahaanForm(forms.Form):
	nama = forms.CharField()
	alamat = forms.CharField()
	email = forms.EmailField()

class editPerusahaanForm(forms.ModelForm):
	class Meta:
		model = Perusahaan
		fields = ['nama_perusahaan','alamat','email',]

class PenilaianForm(forms.ModelForm):
	perusahaan = forms.IntegerField()
	cash_flow = forms.IntegerField()
	proyeksi_keuangan = forms.IntegerField()
	tingkat_revenue = forms.IntegerField()
	bagi_hasil = forms.IntegerField()
	bunga = forms.IntegerField()
	jenis_usaha = forms.IntegerField()
	area_usaha = forms.IntegerField()