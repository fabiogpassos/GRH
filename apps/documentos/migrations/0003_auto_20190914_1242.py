# Generated by Django 2.2.5 on 2019-09-14 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0002_documento_proprietario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='proprietario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='colaboradores.Colaborador'),
            preserve_default=False,
        ),
    ]