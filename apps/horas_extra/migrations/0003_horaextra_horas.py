# Generated by Django 2.2.5 on 2019-10-04 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horas_extra', '0002_horaextra_colaborador'),
    ]

    operations = [
        migrations.AddField(
            model_name='horaextra',
            name='horas',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
            preserve_default=False,
        ),
    ]
