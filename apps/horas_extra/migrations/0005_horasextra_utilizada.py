# Generated by Django 2.2.5 on 2019-10-07 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horas_extra', '0004_auto_20191004_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='horasextra',
            name='utilizada',
            field=models.BooleanField(default=False),
        ),
    ]