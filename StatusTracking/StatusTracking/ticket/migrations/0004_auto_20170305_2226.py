# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-05 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_customer_enduser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='icrequest',
            old_name='contact_person_name',
            new_name='contact_person_name1',
        ),
        migrations.RenameField(
            model_name='icrequest',
            old_name='contact_person_no',
            new_name='contact_person_no1',
        ),
        migrations.RenameField(
            model_name='servicecall',
            old_name='contact_person_name',
            new_name='contact_person_name1',
        ),
        migrations.RenameField(
            model_name='servicecall',
            old_name='contact_person_no',
            new_name='contact_person_no1',
        ),
        migrations.RenameField(
            model_name='servicecall',
            old_name='material_reached_at_site',
            new_name='customer_problem',
        ),
        migrations.RemoveField(
            model_name='icrequest',
            name='no_of_jobs',
        ),
        migrations.RemoveField(
            model_name='servicecall',
            name='no_of_jobs',
        ),
        migrations.RemoveField(
            model_name='servicecall',
            name='pre_sign_off_sheet_status',
        ),
        migrations.RemoveField(
            model_name='servicecall',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='servicecall',
            name='site_status',
        ),
        migrations.AddField(
            model_name='icrequest',
            name='contact_person_name2',
            field=models.CharField(default=0, max_length=255),
        ),
        migrations.AddField(
            model_name='icrequest',
            name='contact_person_no2',
            field=models.IntegerField(default=0, verbose_name=10),
        ),
        migrations.AddField(
            model_name='servicecall',
            name='contact_person_name2',
            field=models.CharField(default=0, max_length=255),
        ),
        migrations.AddField(
            model_name='servicecall',
            name='contact_person_no2',
            field=models.IntegerField(default=0, verbose_name=10),
        ),
        migrations.AlterField(
            model_name='icrequest',
            name='date',
            field=models.DateField(verbose_name='Today'),
        ),
        migrations.AlterField(
            model_name='icrequest',
            name='req_date_of_installation_by_customer',
            field=models.DateField(verbose_name='Req Date Installation of Customer'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='customer_req_date',
            field=models.DateField(verbose_name='Customer Req Date'),
        ),
        migrations.AlterField(
            model_name='servicecall',
            name='date',
            field=models.DateField(verbose_name='Today'),
        ),
        migrations.AlterField(
            model_name='servicecall',
            name='req_date_of_installation_by_customer',
            field=models.DateField(verbose_name='Req Date Installation of Customer'),
        ),
    ]
