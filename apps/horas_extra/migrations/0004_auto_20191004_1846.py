# Generated by Django 2.2.5 on 2019-10-04 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colaboradores', '0004_auto_20190930_2012'),
        ('horas_extra', '0003_horaextra_horas'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HoraExtra',
            new_name='HorasExtra',
        ),
    ]