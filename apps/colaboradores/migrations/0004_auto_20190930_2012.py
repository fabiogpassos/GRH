# Generated by Django 2.2.5 on 2019-09-30 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colaboradores', '0003_auto_20190914_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='empresas.Empresa'),
        ),
    ]