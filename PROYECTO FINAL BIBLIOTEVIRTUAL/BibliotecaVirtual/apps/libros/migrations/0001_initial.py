# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autores', '0002_remove_autor_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('resumen', models.TextField(max_length=300)),
                ('portadas', models.ImageField(upload_to=b'portadas')),
                ('autor', models.ManyToManyField(to='autores.Autor')),
            ],
        ),
    ]
