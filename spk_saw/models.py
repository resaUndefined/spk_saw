# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Jenis(models.Model):
    nama = models.CharField(max_length=15)
    bobot = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name_plural = "Jenis Kriteria"
        ordering = ['nama']

    def __unicode__(self):
        return self.nama

# kriteria kondisi keuangan


class Kondisi_Keuangan(models.Model):
    nama_sub = models.CharField(max_length=50)
    bobot_kriteria = models.DecimalField(max_digits=5, decimal_places=2,
                                         default=0.40)
    target_nilai = models.DecimalField(max_digits=5, decimal_places=2)
    jenis = models.ForeignKey(Jenis, related_name="kondisi_keuangan_jenis", null=True,
                              blank=True)

    class Meta:
        verbose_name_plural = "Kondisi Keuangan"
        ordering = ['pk']

    def __unicode__(self):
        return self.nama_sub


class Cash_Flow(models.Model):
    kondisi_keuangan = models.ForeignKey(Kondisi_Keuangan,
                                         related_name='cash_flow_keuangan',
                                         null=True, blank=True)
    nama_sub = models.CharField(max_length=50, null=True, blank=True)
    bobot_sub = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name_plural = "Sub Kriteria Kondisi Keuangan (Cash Flow)"
        ordering = ['pk']

    def __unicode__(self):
        return self.nama_sub


class Proyeksi_Keuangan(models.Model):
    kondisi_keuangan = models.ForeignKey(Kondisi_Keuangan,
                                         related_name='proyeksi_kondisi_keuangan',
                                         null=True, blank=True)
    nama_sub = models.CharField(max_length=50, null=True, blank=True)
    bobot_sub = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name_plural = "Sub Kriteria Kondisi Keuangan (Proyeksi Keuangan)"
        ordering = ['pk']

    def __unicode__(self):
        return self.nama_sub


class Tingkat_Revenue(models.Model):
    kondisi_keuangan = models.ForeignKey(Kondisi_Keuangan,
                                         related_name='tingkat_revenue_keuangan',
                                         null=True, blank=True)
    nama_sub = models.CharField(max_length=50, null=True, blank=True)
    bobot_sub = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name_plural = "Sub Kriteria Kondisi Keuangan (Tingkat Revenue)"
        ordering = ['pk']

    def __unicode__(self):
        return self.nama_sub
# end kondisi keuangan

# kriteria Investasi Balik


class Inverstasi_Balik(models.Model):
    nama_sub = models.CharField(max_length=50)
    bobot_kriteria = models.DecimalField(max_digits=5, decimal_places=2,
                                         default=0.40)
    target_nilai = models.DecimalField(max_digits=5, decimal_places=2)
    jenis = models.ForeignKey(Jenis, related_name="invstasi_balik_jenis", null=True,
                              blank=True)

    class Meta:
        verbose_name_plural = "Investasi Balik"
        ordering = ['pk']

    def __unicode__(self):
        return self.nama_sub


class Bagi_Hasil(models.Model):
    investasi_balik = models.ForeignKey(Inverstasi_Balik,
                                        related_name='bagi_hasil_investasi',
                                        null=True, blank=True)
    nama_sub = models.CharField(max_length=50, null=True, blank=True)
    bobot_sub = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name_plural = "Sub Kriteria Investasi Balik (Bagi Hasil)"
        ordering = ['pk']

    def __unicode__(self):
        return self.nama_sub


class Bunga(models.Model):
    investasi_balik = models.ForeignKey(Inverstasi_Balik,
                                        related_name='bunga_investasi', null=True,
                                        blank=True)
    nama_sub = models.CharField(max_length=50, null=True, blank=True)
    bobot_sub = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name_plural = "Sub Kriteria Investasi Balik (Bunga)"
        ordering = ['pk']

    def __unicode__(self):
        return self.nama_sub

# end kriteria investasi balik

# kriteria Profile Usaha


class Profile_Usaha(models.Model):
    nama_sub = models.CharField(max_length=50)
    bobot_kriteria = models.DecimalField(max_digits=5, decimal_places=2,
                                         default=0.20)
    target_nilai = models.DecimalField(max_digits=5, decimal_places=2)
    jenis = models.ForeignKey(Jenis, related_name="profil_usaha_jenis", null=True,
                              blank=True)

    class Meta:
        verbose_name_plural = "Profile Usaha"

    def __unicode__(self):
        return self.nama_sub


class Jenis_Usaha(models.Model):
    profile_usaha = models.ForeignKey(Profile_Usaha,
                                      related_name='jenis_usaha_jenis', null=True,
                                      blank=True)
    nama_sub = models.CharField(max_length=50, null=True, blank=True)
    bobot_sub = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name_plural = "Sub Kriteria Profile Usaha (Jenis Usaha)"
        ordering = ['pk']

    def __unicode__(self):
        return self.nama_sub


class Area_Usaha(models.Model):
    profile_usaha = models.ForeignKey(Profile_Usaha,
                                      related_name='area_usaha_jenis', null=True,
                                      blank=True)
    nama_sub = models.CharField(max_length=50, null=True, blank=True)
    bobot_sub = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name_plural = "Sub Kriteria Profile Usaha (Area Usaha)"
        ordering = ['pk']

    def __unicode__(self):
        return self.nama_sub
# end kriteria Profile Usaha

# class Alternatif


class Perusahaan(models.Model):
    nama_perusahaan = models.CharField(max_length=50)
    alamat = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Perusahaan"
        ordering = ['nama_perusahaan']

    def __unicode__(self):
        return self.nama_perusahaan

# class Penilaian Kondisi Keuangan


class Perhitungan_Kondisi_Keuangan(models.Model):
    perusahaan = models.OneToOneField(Perusahaan, related_name='hitung_kondisi_perusahaan',
                                      null=True, blank=True)
    cash_flow = models.ForeignKey(Cash_Flow, related_name='cash_flow_hitung',
                                  null=True, blank=True)
    proyeksi_keuangan = models.ForeignKey(Proyeksi_Keuangan, related_name='proyeksi_keuangan_hitung',
                                          null=True, blank=True)
    tingkat_revenue = models.ForeignKey(Tingkat_Revenue, related_name='tingkat_revenue_hitung',
                                        null=True, blank=True)
    gap1 = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    gap2 = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    gap3 = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    nilai_cf = models.DecimalField(max_digits=5, decimal_places=2, null=True,
                                   blank=True)
    nilai_sf = models.DecimalField(max_digits=5, decimal_places=2, null=True,
                                   blank=True)
    nilai_akhir = models.DecimalField(max_digits=5, decimal_places=2, null=True,
                                      blank=True)

    class Meta:
        verbose_name_plural = "Perhitungan Kondisi Keuangan"
        ordering = ['pk']

    def __unicode__(self):
        return self.perusahaan.nama_perusahaan


class Bobot_Kondisi_Keuangan(models.Model):
    perhitungan_kondisi_keuangan = models.ForeignKey(Perhitungan_Kondisi_Keuangan,
                                                     related_name='kondisi_keuangan_bobot',
                                                     null=True, blank=True)
    bobot = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    jenis = models.ForeignKey(
        Jenis, related_name='jenis_bobot_kondisi', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Bobot Kondisi Keuangan'
        ordering = ['pk']

    def __unicode__(self):
        return self.perhitungan_kondisi_keuangan.__unicode__(self)

# class penilaian tingkat investasi balik


class Perhitungan_Investasi_Balik(models.Model):
    perusahaan = models.OneToOneField(Perusahaan, related_name='investasi_balik_perusahaan',
                                      null=True, blank=True)
    bagi_hasil = models.ForeignKey(Bagi_Hasil, related_name='bagi_hasil_hitung',
                                   null=True, blank=True)
    bunga = models.ForeignKey(Bunga, related_name='bunga_hitung',
                              null=True, blank=True)
    gap1 = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    gap2 = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    nilai_cf = models.DecimalField(max_digits=5, decimal_places=2, null=True,
                                   blank=True)
    nilai_sf = models.DecimalField(max_digits=5, decimal_places=2, null=True,
                                   blank=True)
    nilai_akhir = models.DecimalField(max_digits=5, decimal_places=2, null=True,
                                      blank=True)

    class Meta:
        verbose_name_plural = "Perhitungan Investasi Balik"
        ordering = ['pk']

    def __unicode__(self):
        return self.perusahaan.nama_perusahaan


class Bobot_Investasi_Balik(models.Model):
    perhitungan_investasi_balik = models.ForeignKey(Perhitungan_Investasi_Balik,
                                                    related_name='investasi_balik_bobot',
                                                    null=True, blank=True)
    bobot = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    jenis = models.ForeignKey(
        Jenis, related_name='jenis_bobot_investasi', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Bobot Investasi Balik'
        ordering = ['pk']

    def __unicode__(self):
        return self.perhitungan_investasi_balik.__unicode__(self)


# class penilaian profile usaha
class Perhitungan_Profil_Usaha(models.Model):
    perusahaan = models.OneToOneField(Perusahaan, related_name='profil_usaha_perusahaan',
                                      null=True, blank=True)
    jenis_usaha = models.ForeignKey(Jenis_Usaha, related_name='jenis_usaha_hitung',
                                    null=True, blank=True)
    area_usaha = models.ForeignKey(Area_Usaha, related_name='area_usaha_hitung',
                                   null=True, blank=True)
    gap1 = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    gap2 = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    nilai_cf = models.DecimalField(max_digits=5, decimal_places=2, null=True,
                                   blank=True)
    nilai_sf = models.DecimalField(max_digits=5, decimal_places=2, null=True,
                                   blank=True)
    nilai_akhir = models.DecimalField(max_digits=5, decimal_places=2, null=True,
                                      blank=True)

    class Meta:
        verbose_name_plural = "Perhitungan Profil Usaha"
        ordering = ['pk']

    def __unicode__(self):
        return self.perusahaan.nama_perusahaan


class Bobot_Profil_Usaha(models.Model):
    perhitungan_profil_usaha = models.ForeignKey(Perhitungan_Profil_Usaha,
                                                 related_name='profil_usaha_bobot',
                                                 null=True, blank=True)
    bobot = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    jenis = models.ForeignKey(
        Jenis, related_name='jenis_bobot_profil', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Bobot Profil Usaha'
        ordering = ['pk']

    def __unicode__(self):
        return self.perhitungan_profil_usaha.__unicode__(self)


# class Hasil Ranking
class Hasil(models.Model):
    perusahaan = models.ForeignKey(Perusahaan, related_name='perusahaan_hasil',
                                   null=True, blank=True)
    perhitungan_kondisi_keuangan = models.OneToOneField(Perhitungan_Kondisi_Keuangan,
                                                        related_name='kondisi_keuangan_hasil', null=True,
                                                        blank=True)
    perhitungan_investasi_balik = models.OneToOneField(Perhitungan_Investasi_Balik,
                                                       related_name='investasi_balik_hasil', null=True,
                                                       blank=True)
    perhitungan_profil_usaha = models.OneToOneField(Perhitungan_Profil_Usaha,
                                                    related_name='profil_usaha_hasil', null=True,
                                                    blank=True)
    hasil = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Hasil Perangkingan'
        ordering = ['-hasil']

    def __unicode__(self):
        return self.perusahaan.nama_perusahaan

# from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Publisher(models.Model):
    name = models.CharField(max_length=300)
    num_awards = models.IntegerField()

class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField(null=True,blank=True)

class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)
    registered_users = models.PositiveIntegerField()
