# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-23 18:09
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('countryinfo', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('added_on', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'category_tbl',
            },
        ),
        migrations.CreateModel(
            name='ServiceList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(blank=True, max_length=255, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serviceprovider.Category')),
            ],
            options={
                'db_table': 'service_list_tbl',
            },
        ),
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255, unique=True)),
                ('registered_address', models.CharField(max_length=255)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('service_description', models.CharField(max_length=255)),
                ('email_verified', models.BooleanField(default=False)),
                ('added_on', models.DateTimeField(default=datetime.datetime.now)),
                ('updated_on', models.DateTimeField(default=datetime.datetime.now)),
                ('is_active', models.BooleanField(default=True)),
                ('address', models.ManyToManyField(to='countryinfo.Address')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='provider', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'service_provider_tbl',
            },
        ),
        migrations.CreateModel(
            name='ServiceProviderFixedPayments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0)),
                ('added_on', models.DateTimeField(default=datetime.datetime.now)),
                ('updated_on', models.DateTimeField(default=datetime.datetime.now)),
                ('service_provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serviceprovider.ServiceProvider')),
            ],
            options={
                'db_table': 'service_provider_fixed_payments_tbl',
            },
        ),
        migrations.CreateModel(
            name='ServiceProviderRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(default=datetime.datetime.now)),
                ('updated_on', models.DateTimeField(default=datetime.datetime.now)),
                ('service_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serviceprovider.ServiceList')),
                ('service_provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serviceprovider.ServiceProvider')),
            ],
            options={
                'db_table': 'service_provider_relation_tbl',
            },
        ),
        migrations.AlterUniqueTogether(
            name='serviceproviderrelation',
            unique_together=set([('service_provider', 'service_list')]),
        ),
    ]
