# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-23 18:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('serviceprovider', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(default=datetime.datetime.now)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
                ('service_provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serviceprovider.ServiceProviderRelation')),
            ],
            options={
                'db_table': 'customer_booking_tbl',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0)),
                ('added_on', models.DateTimeField(default=datetime.datetime.now)),
                ('customer_booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.CustomerBooking')),
            ],
            options={
                'db_table': 'transaction_tbl',
            },
        ),
    ]
