# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_auto_20150607_2207'),
        ('image_gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='description_ar',
            field=cms.models.fields.PlaceholderField(slotname=b'description', editable=False, to='cms.Placeholder', null=True, verbose_name='Description'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gallery',
            name='description_de',
            field=cms.models.fields.PlaceholderField(slotname=b'description', editable=False, to='cms.Placeholder', null=True, verbose_name='Description'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gallery',
            name='description_en',
            field=cms.models.fields.PlaceholderField(slotname=b'description', editable=False, to='cms.Placeholder', null=True, verbose_name='Description'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gallery',
            name='description_fa',
            field=cms.models.fields.PlaceholderField(slotname=b'description', editable=False, to='cms.Placeholder', null=True, verbose_name='Description'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gallery',
            name='description_fr',
            field=cms.models.fields.PlaceholderField(slotname=b'description', editable=False, to='cms.Placeholder', null=True, verbose_name='Description'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gallery',
            name='description_pt',
            field=cms.models.fields.PlaceholderField(slotname=b'description', editable=False, to='cms.Placeholder', null=True, verbose_name='Description'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gallery',
            name='title_ar',
            field=models.CharField(max_length=100, null=True, verbose_name='Title'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gallery',
            name='title_de',
            field=models.CharField(max_length=100, null=True, verbose_name='Title'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gallery',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Title'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gallery',
            name='title_fa',
            field=models.CharField(max_length=100, null=True, verbose_name='Title'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gallery',
            name='title_fr',
            field=models.CharField(max_length=100, null=True, verbose_name='Title'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gallery',
            name='title_pt',
            field=models.CharField(max_length=100, null=True, verbose_name='Title'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gallerycategory',
            name='name_ar',
            field=models.CharField(max_length=256, null=True, verbose_name='Name'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gallerycategory',
            name='name_de',
            field=models.CharField(max_length=256, null=True, verbose_name='Name'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gallerycategory',
            name='name_en',
            field=models.CharField(max_length=256, null=True, verbose_name='Name'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gallerycategory',
            name='name_fa',
            field=models.CharField(max_length=256, null=True, verbose_name='Name'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gallerycategory',
            name='name_fr',
            field=models.CharField(max_length=256, null=True, verbose_name='Name'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gallerycategory',
            name='name_pt',
            field=models.CharField(max_length=256, null=True, verbose_name='Name'),
            preserve_default=True,
        ),
    ]
