# Generated by Django 2.1.2 on 2018-12-02 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70)),
                ('costo_presupuesto', models.IntegerField(blank=True)),
                ('costo_real', models.IntegerField(blank=True)),
                ('notas', models.TextField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('sucursal', models.CharField(max_length=80)),
                ('direccion', models.CharField(max_length=80)),
                ('ciudad', models.ManyToManyField(max_length=80, to='compras.Ciudad')),
                ('region', models.ManyToManyField(max_length=80, to='compras.Region')),
            ],
        ),
        migrations.AddField(
            model_name='productos',
            name='tienda',
            field=models.ManyToManyField(to='compras.Tienda'),
        ),
    ]
