# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-08 21:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='thistrans', max_length=50)),
                ('active', models.BooleanField(default=1)),
                ('begin', models.DateTimeField(auto_now_add=True)),
                ('lasttouched', models.DateTimeField(auto_now_add=True)),
                ('contentClass', models.CharField(default='', max_length=500)),
                ('contentDescription', models.CharField(max_length=100, null=True)),
                ('contentSize', models.CharField(max_length=100, null=True)),
                ('contentWeight', models.CharField(max_length=100, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='writer', to=settings.AUTH_USER_MODEL)),
                ('currentHolder', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='holder', to=settings.AUTH_USER_MODEL)),
                ('recipient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TransportLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='thisloco', max_length=50)),
                ('locationname', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=500, null=True)),
                ('streetnr', models.CharField(max_length=500, null=True)),
                ('zip', models.CharField(max_length=500, null=True)),
                ('city', models.CharField(max_length=500, null=True)),
                ('country', models.CharField(max_length=500, null=True)),
                ('geoLat', models.DecimalField(decimal_places=10, default=0, max_digits=19, null=True)),
                ('geoLon', models.DecimalField(decimal_places=10, default=0, max_digits=19, null=True)),
                ('lastused', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authorlocation', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TransportPass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('touched', models.DateTimeField(auto_now_add=True)),
                ('points', models.PositiveSmallIntegerField(default=1, null=True)),
                ('location', models.CharField(max_length=100, null=True)),
                ('locationLat', models.CharField(max_length=100, null=True)),
                ('locationLon', models.CharField(max_length=100, null=True)),
                ('logdump', models.CharField(max_length=1000, null=True)),
                ('newcurrentHolder', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='newholder', to=settings.AUTH_USER_MODEL)),
                ('transport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kohrsupply.Transport')),
            ],
        ),
        migrations.CreateModel(
            name='TransportUserGetFet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('getfet', models.CharField(choices=[('sleeping', 'Sleeping'), ('carrying', 'Carrying'), ('hubbing', 'Hubbing'), ('flooding', 'only Flooding'), ('grabbing', 'only Grabbing')], default='grabbing', max_length=8)),
                ('changed', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TransportUserLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('changed', models.DateTimeField(auto_now_add=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kohrsupply.TransportLocation')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
