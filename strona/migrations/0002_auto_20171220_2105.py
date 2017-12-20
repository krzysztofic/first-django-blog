# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Nazwa Kategorii')),
                ('slug', models.SlugField(max_length=100, verbose_name='Odnośnik', unique=True)),
            ],
            options={
                'verbose_name_plural': 'Kategorie',
                'verbose_name': 'Kategoria',
            },
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Tytuł'),
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(verbose_name='Kategorie', to='strona.Category'),
        ),
    ]
