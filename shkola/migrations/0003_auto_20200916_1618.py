# Generated by Django 3.1.1 on 2020-09-16 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shkola', '0002_auto_20200916_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='NomeraKlassa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomer_klassa', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Predmety',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazvanie_predmeta', models.TextField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Prepodavately',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imya', models.TextField(max_length=50)),
                ('otchestvo', models.TextField(max_length=50)),
                ('familiya', models.TextField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='uroki',
            name='nazvanie_predmeta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shkola.predmety'),
        ),
        migrations.AlterField(
            model_name='uroki',
            name='nomer_klassa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shkola.nomeraklassa'),
        ),
        migrations.AlterField(
            model_name='uroki',
            name='prepodavatel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shkola.prepodavately'),
        ),
    ]