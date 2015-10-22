# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama', models.CharField(max_length=100)),
                ('alamat', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Data Member',
            },
        ),
        migrations.CreateModel(
            name='Paket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama', models.CharField(max_length=30)),
                ('keterangan', models.TextField()),
                ('status', models.BooleanField()),
                ('harga', models.IntegerField()),
            ],
            options={
                'verbose_name': 'pizza',
                'verbose_name_plural': 'Master Paket',
            },
        ),
        migrations.CreateModel(
            name='Pembayaran',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jenis', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Master Pembayaran',
            },
        ),
        migrations.CreateModel(
            name='Wilayah',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama', models.CharField(unique=True, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='paket',
            field=models.ForeignKey(to='registrasi.Paket'),
        ),
        migrations.AddField(
            model_name='member',
            name='pembayaran',
            field=models.ForeignKey(to='registrasi.Pembayaran'),
        ),
        migrations.AddField(
            model_name='member',
            name='wilayah',
            field=models.ForeignKey(to='registrasi.Wilayah'),
        ),
    ]
