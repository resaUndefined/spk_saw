# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from spk_saw.models import Jenis,Kondisi_Keuangan,Cash_Flow,Proyeksi_Keuangan,Tingkat_Revenue,Inverstasi_Balik,Bagi_Hasil,Bunga,Profile_Usaha,Jenis_Usaha,Area_Usaha,Perusahaan,Perhitungan_Kondisi_Keuangan,Bobot_Kondisi_Keuangan,Perhitungan_Investasi_Balik,Bobot_Investasi_Balik,Perhitungan_Profil_Usaha,Bobot_Profil_Usaha,Hasil,Author,Publisher,Book,Store
# Register your models here.
class JenisAdmin(admin.ModelAdmin):
	list_per_page = 10
	list_display = ('id','nama','bobot',)
	search_fields = ('nama',)


class Cash_FlowInline(admin.TabularInline):
	model = Cash_Flow


class Proyeksi_KeuanganInline(admin.TabularInline):
	model = Proyeksi_Keuangan


class Tingkat_RevenueInline(admin.TabularInline):
	model = Tingkat_Revenue


class Kondisi_KeuanganAdmin(admin.ModelAdmin):
	list_per_page = 15
	list_display = ('nama_sub','bobot_kriteria','target_nilai','jenis',)
	search_fields = ('nama_sub',)
	inlines = [Cash_FlowInline,Proyeksi_KeuanganInline,Tingkat_RevenueInline]


class Bagi_HasilInline(admin.TabularInline):
	model = Bagi_Hasil


class BungaInline(admin.TabularInline):
	model = Bunga


class Investasi_BalikAdmin(admin.ModelAdmin):
	list_per_page = 15
	list_display = ('nama_sub','bobot_kriteria','target_nilai','jenis',)
	search_fields = ('nama_sub',)
	inlines = [Bagi_HasilInline,BungaInline]


class Jenis_UsahaInline(admin.TabularInline):
	model = Jenis_Usaha


class Area_UsahaInline(admin.TabularInline):
	model = Area_Usaha


class Profile_UsahaAdmin(admin.ModelAdmin):
	list_per_page = 15
	list_display = ('nama_sub','bobot_kriteria','target_nilai','jenis',)
	search_fields = ('nama_sub',)
	inlines = [Jenis_UsahaInline,Area_UsahaInline]


class PerusahaanAdmin(admin.ModelAdmin):
	list_per_page = 15
	list_display = ('nama_perusahaan','alamat','email',)
	search_fields = ('nama_perusahaan',)



admin.site.site_header = 'SPK Pemilihan Investor'
admin.site.register(Jenis,JenisAdmin)
admin.site.register(Kondisi_Keuangan,Kondisi_KeuanganAdmin)
admin.site.register(Inverstasi_Balik,Investasi_BalikAdmin)
admin.site.register(Profile_Usaha,Profile_UsahaAdmin)
admin.site.register(Perusahaan,PerusahaanAdmin)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Store)