# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_gallery', '0002_auto_20151217_0446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='description_de',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='description_fa',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='description_pt',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='title_de',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='title_fa',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='title_pt',
        ),
        migrations.RemoveField(
            model_name='gallerycategory',
            name='name_de',
        ),
        migrations.RemoveField(
            model_name='gallerycategory',
            name='name_fa',
        ),
        migrations.RemoveField(
            model_name='gallerycategory',
            name='name_pt',
        ),
        migrations.AddField(
            model_name='galleryplugin',
            name='template',
            field=models.CharField(blank=True, max_length=256, choices=[(b'image_gallery/partials/gallery.html', 'Default'), (b'image_gallery/partials/test_template.html', 'Test Template')]),
        ),
    ]
