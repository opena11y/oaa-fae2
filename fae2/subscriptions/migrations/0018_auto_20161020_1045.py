# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-20 15:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0017_institutionalsubscription_alt_domain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institutionalsubscription',
            name='account_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='institional_subscriptions', to='accounts.AccountType'),
        ),
    ]