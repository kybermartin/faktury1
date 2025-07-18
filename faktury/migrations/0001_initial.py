# Generated by Django 5.2.1 on 2025-05-11 18:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cislo_faktury', models.CharField(max_length=20, unique=True)),
                ('datum_vystavenia', models.DateField()),
                ('datum_splatnosti', models.DateField()),
                ('odberatel', models.CharField(max_length=255)),
                ('suma_celkom', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stav_platby', models.CharField(choices=[('zaplatená', 'Zaplatená'), ('nezaplatená', 'Nezaplatená')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazov', models.CharField(max_length=255)),
                ('mnozstvo', models.IntegerField()),
                ('cena_za_jednotku', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sadzba_dph', models.IntegerField()),
                ('faktura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='polozky', to='faktury.invoice')),
            ],
        ),
    ]
