# Generated by Django 2.0 on 2018-02-02 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('madadju', '0001_initial'),
        ('hamyar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adapt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='hamyar',
            name='report_method',
            field=models.IntegerField(choices=[(0, 'text'), (1, 'email')]),
        ),
        migrations.AddField(
            model_name='payment',
            name='hamyar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hamyar.Hamyar'),
        ),
        migrations.AddField(
            model_name='payment',
            name='madadju',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='madadju.Madadju'),
        ),
        migrations.AddField(
            model_name='adapt',
            name='hamyar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hamyar.Hamyar'),
        ),
        migrations.AddField(
            model_name='adapt',
            name='madadju',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='madadju.Madadju'),
        ),
    ]