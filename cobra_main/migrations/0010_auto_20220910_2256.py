# Generated by Django 3.2.5 on 2022-09-11 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cobra_main', '0009_auto_20220910_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productogenerado',
            name='diseño',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cobra_main.diseño'),
        ),
        migrations.AlterField(
            model_name='productogenerado',
            name='producto',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cobra_main.producto'),
        ),
    ]