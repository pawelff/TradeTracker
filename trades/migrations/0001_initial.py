# Generated by Django 4.1.5 on 2023-01-31 18:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Strategy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('profit', models.FloatField()),
                ('currency', models.CharField(max_length=5)),
                ('dolar_profit', models.DecimalField(decimal_places=2, max_digits=7)),
                ('strategy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trades.strategy')),
            ],
        ),
    ]