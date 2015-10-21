# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('user_ptr', models.OneToOneField(to=settings.AUTH_USER_MODEL, auto_created=True, primary_key=True, serialize=False, parent_link=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Paket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=30)),
                ('harga', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pembayaran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis', models.CharField(max_length=30)),
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
    ]
