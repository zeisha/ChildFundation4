# Generated by Django 2.0 on 2018-02-05 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hamyar', '0006_auto_20180204_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentfoundation',
            name='receipt_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='hamyar',
            name='report_method',
            field=models.IntegerField(choices=[(0, 'text'), (1, 'email')]),
        ),
    ]
