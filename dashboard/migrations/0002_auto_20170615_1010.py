# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-15 10:10
from __future__ import unicode_literals

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='languages',
            options={'verbose_name': 'Language'},
        ),
        migrations.AlterModelOptions(
            name='languageset',
            options={'verbose_name': 'Language Set'},
        ),
        migrations.AlterModelOptions(
            name='packages',
            options={'verbose_name': 'Package'},
        ),
        migrations.AlterModelOptions(
            name='releasestream',
            options={'verbose_name': 'Release Stream'},
        ),
        migrations.AlterModelOptions(
            name='streambranches',
            options={'verbose_name_plural': 'Release Branches'},
        ),
        migrations.AlterModelOptions(
            name='transplatform',
            options={'verbose_name': 'Translation Platform'},
        ),
        migrations.AddField(
            model_name='packages',
            name='translation_file_ext',
            field=models.CharField(blank=True, default='po', max_length=10, null=True, verbose_name='Translation Format (po)'),
        ),
        migrations.AddField(
            model_name='packages',
            name='upstream_lastupdated',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='packages',
            name='upstream_latest_stats',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='transplatform',
            name='auth_login_id',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Auth User'),
        ),
        migrations.AddField(
            model_name='transplatform',
            name='auth_token_key',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Auth Token'),
        ),
        migrations.AlterField(
            model_name='packages',
            name='package_name',
            field=models.CharField(max_length=1000, unique=True, verbose_name='Package Name'),
        ),
        migrations.AlterField(
            model_name='packages',
            name='release_branch_mapping',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='packages',
            name='release_streams',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=400), default=list, null=True, size=None, verbose_name='Release Streams'),
        ),
        migrations.AlterField(
            model_name='packages',
            name='transplatform_name',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Package Name at Translation Platform'),
        ),
        migrations.AlterField(
            model_name='packages',
            name='transplatform_slug',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.TransPlatform', to_field='platform_slug', verbose_name='Translation Platform'),
        ),
        migrations.AlterField(
            model_name='packages',
            name='transplatform_url',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='Translation Platform Project URL'),
        ),
        migrations.AlterField(
            model_name='packages',
            name='upstream_name',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Upstream Name'),
        ),
        migrations.AlterField(
            model_name='packages',
            name='upstream_url',
            field=models.URLField(max_length=2000, unique=True, verbose_name='Upstream URL'),
        ),
        migrations.AlterField(
            model_name='streambranches',
            name='calendar_url',
            field=models.URLField(max_length=500, null=True, verbose_name='Calender iCal URL'),
        ),
        migrations.AlterField(
            model_name='streambranches',
            name='current_phase',
            field=models.CharField(max_length=200, null=True, verbose_name='Current Phase'),
        ),
        migrations.AlterField(
            model_name='streambranches',
            name='lang_set',
            field=models.CharField(max_length=200, verbose_name='Language Set'),
        ),
        migrations.AlterField(
            model_name='streambranches',
            name='notifications_flag',
            field=models.BooleanField(default=True, verbose_name='Notification'),
        ),
        migrations.AlterField(
            model_name='streambranches',
            name='relbranch_name',
            field=models.CharField(max_length=500, verbose_name='Release Branch Name'),
        ),
        migrations.AlterField(
            model_name='streambranches',
            name='relbranch_slug',
            field=models.CharField(max_length=500, unique=True, verbose_name='Release Branch Slug'),
        ),
        migrations.AlterField(
            model_name='streambranches',
            name='relstream_slug',
            field=models.CharField(max_length=400, verbose_name='Release Stream Slug'),
        ),
        migrations.AlterField(
            model_name='streambranches',
            name='scm_branch',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='SCM Branch Name'),
        ),
        migrations.AlterField(
            model_name='streambranches',
            name='sync_calendar',
            field=models.BooleanField(default=True, verbose_name='Sync Calender'),
        ),
        migrations.AlterField(
            model_name='streambranches',
            name='track_trans_flag',
            field=models.BooleanField(default=True, verbose_name='Track Translation'),
        ),
    ]
