# Generated by Django 3.1.1 on 2020-09-18 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200918_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='familiya',
            field=models.TextField(default='-', max_length=50),
        ),
        migrations.AddField(
            model_name='customuser',
            name='imya',
            field=models.TextField(default='-', max_length=50),
        ),
    ]
