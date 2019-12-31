# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from spk_saw.forms import tambahPerusahaanForm,editPerusahaanForm,PenilaianForm
from spk_saw.models import Perusahaan,Cash_Flow,Proyeksi_Keuangan,Tingkat_Revenue,Bagi_Hasil,Bunga,Jenis_Usaha,Area_Usaha
from spk_saw.models import Perhitungan_Kondisi_Keuangan,Perhitungan_Profil_Usaha,Perhitungan_Investasi_Balik
from spk_saw.models import Kondisi_Keuangan,Inverstasi_Balik,Profile_Usaha
# from spk_saw.forms import PenilaianForm,NilaiForm
# from spk_saw.models import Hotel,Harga_Sewa,Lokasi,Fasilitas,Kelas_Hotel,Nilai
# from sistem_pakar.forms import SignUpForm,MemberForm,KonsultasiForm
# from django.contrib.auth.forms import PasswordChangeForm
# from django.contrib.auth import update_session_auth_hash
# from sistem_pakar.models import Relasi, Diagnosa, Kerusakan
# import datetime

# Create your views here.
def Index (request):

	return render(request, 'login.html')


def LogoutView(request):
	
	logout(request)

	return redirect('/')


def Pengguna(request):
	data = {
				'user' : request.user,
			}
	if request.user.is_authenticated():
		
		return render(request,'index2.html',data)
	else:
		return render(request, 'login.html',data)


def PanelPengguna(request):
	data = {
		'user' : request.user,
	}
	if request.user.is_authenticated():
		return render(request,'index2.html',data)

	if request.POST:
		username = request.POST.get('uname')
		password = request.POST.get('pass')
		is_auth = authenticate(username=username,password=password)
		if is_auth is not None:
			login(request,is_auth)
			data = {
				'user' : request.user,
			}

			return render(request,'index2.html',data)
		else:
			messages.warning(
				request, 'Gagal, Silakan cek user dan password anda'
				)
	return render(request,'login.html')


def hakAksesView(request):
	data = {
		'user' : request.user,
	}
	return render(request, 'member_ubah.html',data)


# @login_required(login_url='/login/')
def hakAksesViewUbah(request):
	form = PasswordChangeForm(request.user)
	data = {
		'user' : request.user,
		'form' : form,
	}
	return render(request, 'member-ubah-pw.html',data)


# @login_required(login_url='/login/')
def hakAksesUbah(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)  # Important!
			messages.success(request, 'Your password was successfully updated!')
			return redirect('/login/')
		else:
			messages.error(request, 'Please correct the error below.')
	else:
		form = PasswordChangeForm(request.user)
		return render(request, 'member-ubah-pw.html', {
			'form': form
			})


def PerusahaanView(request):
	prs = Perusahaan.objects.all()
	data = {
		'prs' : prs,
	}
	return render(request,'perusahaan-view.html',data)


def tambahPerusahaan(request):
	if request.method == 'POST':
		form = tambahPerusahaanForm(request.POST)
		if form.is_valid():
			prshn = request.POST.get('nama')
			almt = request.POST.get('alamat')
			eml = request.POST.get('email')
			prshn_obj = Perusahaan(nama_perusahaan=prshn,alamat=almt,email=eml)
			prshn_obj.save()
			messages.success(request, 'Success!')
			return redirect('/login/pengguna/perusahaan/')
		else:
			messages.error(
				request,'Please fill the columns with the correct values!')
	else:
		data = {
		'user' : request.user,
		}
	return render(request,'perusahaan.html',data)

def editPerusahaan(request,id):
	data_perusahaan = Perusahaan.objects.get(id=id)
	if request.method == 'POST':
		form = editPerusahaanForm(request.POST,instance=data_perusahaan)
		if form.is_valid():
			form.save()
			messages.success(request, 'Success!')
			return redirect('/login/pengguna/perusahaan/')
		else:
			messages.error(
				request,'Please fill the columns with the correct values!')
	else:
		# perusahaan = Perusahaan.objects.get(id=id)
		form = editPerusahaanForm(instance=data_perusahaan)
		data = {
		'user' : request.user,
		'form' : form,
		}
	return render(request,'perusahaan-edit.html',data)

def deletePerusahaan(request, id):
	data_perusahaan = Perusahaan.objects.get(id=id)
	data_perusahaan.delete()
	return redirect('/login/pengguna/perusahaan/')

def Menilai(request):
	if request.method == 'POST':
		form = PenilaianForm(request.POST)
		if form.is_valid():
			perusahaan = request.POST.get('perusahaan')
			cash_flow = request.POST.get('cash_flow')
			proyeksi_keuangan = request.POST.get('proyeksi_keuangan')
			tingkat_revenue = request.POST.get('tingkat_revenue')
			bagi_hasil = request.POST.get('bagi_hasil')
			bunga = request.POST.get('bunga')
			jenis_usaha = request.POST.get('jenis_usaha')
			area_usaha = request.POST.get('area_usaha')
			htg_kondisi_obj = Perhitungan_Kondisi_Keuangan(
								perusahaan=perusahaan,cash_flow=cash_flow,
								proyeksi_keuangan=proyeksi_keuangan,
								tingkat_revenue=tingkat_revenue
										)
			
			htg_investasi_obj = Perhitungan_Investasi_Balik(
								perusahaan=perusahaan,bagi_hasil=bagi_hasil,
								bunga=bunga)
			
			htg_profil_obj = Perhitungan_Profil_Usaha(
								perusahaan=perusahaan,jenis_usaha=jenis_usaha,
								area_usaha=area_usaha)
			htg_kondisi_obj.save(commit=False)
			htg_investasi_obj.save(commit=False)
			htg_investasi_obj.save(commit=False)
			
			k_htg1 = Cash_Flow.objects.get(pk=cash_flow)
			k_htg2 = Proyeksi_Keuangan.objects.get(pk=proyeksi_keuangan)
			k_htg3 = Tingkat_Revenue.objects.get(pk=tingkat_revenue) 
			kondisi1 = Kondisi_Keuangan.objects.get(pk=1)
			kondisi2 = Kondisi_Keuangan.objects.get(pk=2)
			kondisi3 = Kondisi_Keuangan.objects.get(pk=3)
			k_gap1 = k_htg1.bobot_sub - kondisi1.target_nilai
			k_gap2 = k_htg2.bobot_sub - kondisi2.target_nilai
			k_gap3 = k_htg3.bobot_sub - kondisi3.target_nilai

			investasi1 = Inverstasi_Balik.objects.get(pk=1)
			investasi2 = Inverstasi_Balik.objects.get(pk=2)
			i_htg1 = Bagi_Hasil.objects.get(pk=bagi_hasil)
			i_htg2 = Bunga.objects.get(pk=bunga)
			i_gap1 = i_htg1.bobot_sub -investasi1
			i_gap2 = i_htg2.bobot_sub - investasi2

			profil1 = Profile_Usaha.objects.get(pk=1)
			profil2 = Profile_Usaha.objects.get(pk=2)
			p_htg1 = Jenis_Usaha.objects.get(pk=jenis_usaha)
			p_htg2 = Area_Usaha.objects.get(pk=area_usaha)
			p_gap1 = p_htg1.bobot_sub - profil1
			p_gap2 = p_htg2.bobot_sub - profil2
			if k_gap1 == 0.00:
				k_gap1 = 5.00
			elif k_gap1 == 1.00:
				k_gap1 == 5.00
			elif k_gap1 == -1.00:
				k_gap1 == 4.00
			elif k_gap1 == 2.00:
				k+k_gap1 == 5.00
			elif k_gap1 == -2.00:
				k_gap1 = 3.00
			elif k_gap1 == 3.00:
				k_gap1 = 5.00
			elif k_gap1 == -3.00:
				k_gap1 = 2.00
			elif k_gap1 == 4.00:
				k_gap1 = 5.00
			elif k_gap1 == -4.00:
				k_gap1 = 1
			endif

	else:
		PERUSAHAAN = Perusahaan.objects.all()
		CASH_FLOW = Cash_Flow.objects.all()
		PROYEKSI_KEUANGAN = Proyeksi_Keuangan.objects.all()
		TINGKAT_REVENUE = Tingkat_Revenue.objects.all()
		BAGI_HASIL = Bagi_Hasil.objects.all()
		BUNGA = Bunga.objects.all()
		JENIS_USAHA = Jenis_Usaha.objects.all()
		AREA_USAHA = Area_Usaha.objects.all()
		data = {
			'PERUSAHAAN' : PERUSAHAAN,
			'CASH_FLOW' : CASH_FLOW,
			'PROYEKSI_KEUANGAN' : PROYEKSI_KEUANGAN,
			'TINGKAT_REVENUE' : TINGKAT_REVENUE,
			'BAGI_HASIL' : BAGI_HASIL,
			'BUNGA' : BUNGA,
			'JENIS_USAHA' : JENIS_USAHA,
			'AREA_USAHA' : AREA_USAHA,
		}
	return render(request,'nilai.html',data)
