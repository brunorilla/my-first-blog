# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_categoria_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100, choices=[(b'El Capital', b'El Capital'), (b'Rebelion en la granja', b'Rebelion en la granja'), (b'Big Sur', b'Big Sur'), (b'Factotum', b'Factotum'), (b'Espera a la primavera, Bandini', b'Espera a la primavera, Bandini'), (b'History of France', b'History of France'), (b'PHP manual', b'PHP manual'), (b'La vida en rojo', b'La vida en rojo')])),
            ],
        ),
    ]
