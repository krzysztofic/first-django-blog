# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0002_auto_20171220_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.ImageField(blank=True, upload_to='icons', verbose_name='Ikonka Kategorii'),
        ),
    ]
