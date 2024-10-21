# Generated by Django 5.1.2 on 2024-10-21 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(choices=[('Argentina', 'Argentina'), ('Brasil', 'Brasil'), ('Chile', 'Chile')], max_length=50)),
                ('forma_venta', models.CharField(choices=[('Online', 'Online'), ('Presencial', 'Presencial')], max_length=50)),
                ('forma_pago', models.CharField(choices=[('Efectivo', 'Efectivo'), ('Tarjeta de Crédito', 'Tarjeta de Crédito'), ('Transferencia', 'Transferencia')], max_length=50)),
                ('producto', models.CharField(max_length=100)),
                ('vendedor', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('ventas', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cantidad', models.PositiveIntegerField()),
                ('comision', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
