# Generated by Django 2.1.2 on 2018-12-03 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tienda',
            name='ciudad',
            field=models.ManyToManyField(to='compras.Ciudad'),
        ),
        migrations.AlterField(
            model_name='tienda',
            name='region',
            field=models.ManyToManyField(to='compras.Region'),
        ),
    ]