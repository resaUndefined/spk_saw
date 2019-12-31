# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-04 00:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area_Usaha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_sub', models.CharField(blank=True, max_length=50, null=True)),
                ('bobot_sub', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'ordering': ['pk'],
                'verbose_name_plural': 'Sub Kriteria Profile Usaha (Area Usaha)',
            },
        ),
        migrations.CreateModel(
            name='Bagi_Hasil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_sub', models.CharField(blank=True, max_length=50, null=True)),
                ('bobot_sub', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'ordering': ['pk'],
                'verbose_name_plural': 'Sub Kriteria Investasi Balik (Bagi Hasil)',
            },
        ),
        migrations.CreateModel(
            name='Bunga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_sub', models.CharField(blank=True, max_length=50, null=True)),
                ('bobot_sub', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'ordering': ['pk'],
                'verbose_name_plural': 'Sub Kriteria Investasi Balik (Bunga)',
            },
        ),
        migrations.CreateModel(
            name='Cash_Flow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_sub', models.CharField(blank=True, max_length=50, null=True)),
                ('bobot_sub', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'ordering': ['pk'],
                'verbose_name_plural': 'Sub Kriteria Kondisi Keuangan (Cash Flow)',
            },
        ),
        migrations.CreateModel(
            name='Inverstasi_Balik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_sub', models.CharField(max_length=50)),
                ('bobot_kriteria', models.DecimalField(decimal_places=2, default=0.4, max_digits=5)),
                ('target_nilai', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'ordering': ['pk'],
                'verbose_name_plural': 'Investasi Balik',
            },
        ),
        migrations.CreateModel(
            name='Jenis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=15)),
                ('bobot', models.DecimalField(decimal_places=4, max_digits=5)),
            ],
            options={
                'ordering': ['nama'],
                'verbose_name_plural': 'Jenis Kriteria',
            },
        ),
        migrations.CreateModel(
            name='Jenis_Usaha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_sub', models.CharField(blank=True, max_length=50, null=True)),
                ('bobot_sub', models.DecimalField(decimal_places=2, max_digits=5)),
                ('jenis', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jenis_usaha_jenis', to='spk_saw.Jenis')),
            ],
            options={
                'ordering': ['pk'],
                'verbose_name_plural': 'Sub Kriteria Profile Usaha (Jenis Usaha)',
            },
        ),
        migrations.CreateModel(
            name='Kondisi_Keuangan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_sub', models.CharField(max_length=50)),
                ('bobot_kriteria', models.DecimalField(decimal_places=2, default=0.4, max_digits=5)),
                ('target_nilai', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'ordering': ['pk'],
                'verbose_name_plural': 'Kondisi Keuangan',
            },
        ),
        migrations.CreateModel(
            name='Perhitungan_Investasi_Balik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gap1', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('gap2', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('nilai_cf', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('nilai_sf', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('nilai_akhir', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('bagi_hasil', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bagi_hasil_hitung', to='spk_saw.Bagi_Hasil')),
                ('bunga', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bunga_hitung', to='spk_saw.Bunga')),
            ],
            options={
                'verbose_name_plural': 'Perhitungan Investasi Balik',
            },
        ),
        migrations.CreateModel(
            name='Perhitungan_Kondisi_Keuangan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gap1', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('gap2', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('gap3', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('nilai_cf', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('nilai_sf', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('nilai_akhir', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('cash_flow', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cash_flow_hitung', to='spk_saw.Cash_Flow')),
            ],
            options={
                'verbose_name_plural': 'Perhitungan Kondisi Keuangan',
            },
        ),
        migrations.CreateModel(
            name='Perhitungan_Profil_Usaha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gap1', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('gap2', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('nilai_cf', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('nilai_sf', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('nilai_akhir', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('area_usaha', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='area_usaha_hitung', to='spk_saw.Area_Usaha')),
                ('jenis_usaha', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jenis_usaha_hitung', to='spk_saw.Jenis_Usaha')),
            ],
            options={
                'verbose_name_plural': 'Perhitungan Profil Usaha',
            },
        ),
        migrations.CreateModel(
            name='Perusahaan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_perusahaan', models.CharField(max_length=50)),
                ('alamat', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
            ],
            options={
                'ordering': ['nama_perusahaan'],
                'verbose_name_plural': 'Perusahaan',
            },
        ),
        migrations.CreateModel(
            name='Profile_Usaha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_sub', models.CharField(max_length=50)),
                ('bobot_kriteria', models.DecimalField(decimal_places=2, default=0.3, max_digits=5)),
                ('target_nilai', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'verbose_name_plural': 'Profile Usaha',
            },
        ),
        migrations.CreateModel(
            name='Proyeksi_Keuangan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_sub', models.CharField(blank=True, max_length=50, null=True)),
                ('bobot_sub', models.DecimalField(decimal_places=2, max_digits=5)),
                ('jenis', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proyeksi_keuangan_jenis', to='spk_saw.Jenis')),
                ('kondisi_keuangan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proyeksi_kondisi_keuangan', to='spk_saw.Kondisi_Keuangan')),
            ],
            options={
                'ordering': ['pk'],
                'verbose_name_plural': 'Sub Kriteria Kondisi Keuangan (Proyeksi Keuangan)',
            },
        ),
        migrations.CreateModel(
            name='Tingkat_Revenue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_sub', models.CharField(blank=True, max_length=50, null=True)),
                ('bobot_sub', models.DecimalField(decimal_places=2, max_digits=5)),
                ('jenis', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tingkat_revenue_jenis', to='spk_saw.Jenis')),
                ('kondisi_keuangan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tingkat_revenue_keuangan', to='spk_saw.Kondisi_Keuangan')),
            ],
            options={
                'ordering': ['pk'],
                'verbose_name_plural': 'Sub Kriteria Kondisi Keuangan (Tingkat Revenue)',
            },
        ),
        migrations.AddField(
            model_name='perhitungan_profil_usaha',
            name='perusahaan',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profil_usaha_perusahaan', to='spk_saw.Perusahaan'),
        ),
        migrations.AddField(
            model_name='perhitungan_kondisi_keuangan',
            name='perusahaan',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hitung_kondisi_perusahaan', to='spk_saw.Perusahaan'),
        ),
        migrations.AddField(
            model_name='perhitungan_kondisi_keuangan',
            name='proyeksi_keuangan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proyeksi_keuangan_hitung', to='spk_saw.Proyeksi_Keuangan'),
        ),
        migrations.AddField(
            model_name='perhitungan_kondisi_keuangan',
            name='tingkat_revenue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tingkat_revenue_hitung', to='spk_saw.Tingkat_Revenue'),
        ),
        migrations.AddField(
            model_name='perhitungan_investasi_balik',
            name='perusahaan',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='investasi_balik_perusahaan', to='spk_saw.Perusahaan'),
        ),
        migrations.AddField(
            model_name='jenis_usaha',
            name='profile_usaha',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jenis_usaha_jenis', to='spk_saw.Profile_Usaha'),
        ),
        migrations.AddField(
            model_name='cash_flow',
            name='jenis',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cash_flow_jenis', to='spk_saw.Jenis'),
        ),
        migrations.AddField(
            model_name='cash_flow',
            name='kondisi_keuangan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cash_flow_keuangan', to='spk_saw.Kondisi_Keuangan'),
        ),
        migrations.AddField(
            model_name='bunga',
            name='investasi_balik',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bunga_investasi', to='spk_saw.Inverstasi_Balik'),
        ),
        migrations.AddField(
            model_name='bunga',
            name='jenis',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bunga_jenis', to='spk_saw.Jenis'),
        ),
        migrations.AddField(
            model_name='bagi_hasil',
            name='investasi_balik',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bagi_hasil_investasi', to='spk_saw.Inverstasi_Balik'),
        ),
        migrations.AddField(
            model_name='bagi_hasil',
            name='jenis',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bagi_hasil_jenis', to='spk_saw.Jenis'),
        ),
        migrations.AddField(
            model_name='area_usaha',
            name='jenis',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='area_usaha_jenis', to='spk_saw.Jenis'),
        ),
        migrations.AddField(
            model_name='area_usaha',
            name='profile_usaha',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='area_usaha_jenis', to='spk_saw.Profile_Usaha'),
        ),
    ]
