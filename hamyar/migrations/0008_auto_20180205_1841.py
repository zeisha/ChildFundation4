# Generated by Django 2.0.1 on 2018-02-05 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hamyar', '0007_auto_20180205_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hamyar',
            name='report_method',
            field=models.IntegerField(choices=[(1, 'email'), (0, 'text')]),
        ),
    ]
