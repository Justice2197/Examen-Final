# Generated by Django 2.1.2 on 2018-12-10 03:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0004_auto_20181209_2342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tienda',
            name='region',
        ),
        migrations.AddField(
            model_name='ciudad',
            name='region',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='compras.Region'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ciudad',
            name='nombre',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='region',
            name='nombre',
            field=models.CharField(max_length=40),
        ),
    ]
