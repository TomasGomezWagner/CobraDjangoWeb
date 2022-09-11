# Generated by Django 3.2.5 on 2022-09-11 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cobra_main', '0007_auto_20220910_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductoGenerado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_generado', models.CharField(choices=[('Generado', 'Generado'), ('Pagado', 'Pagado'), ('Enviado', 'Enviado')], default='Gereado', max_length=20, verbose_name='Estado')),
                ('diseño', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cobra_main.diseño')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cobra_main.producto')),
            ],
        ),
    ]