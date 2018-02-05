# Generated by Django 2.0.1 on 2018-02-05 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('madadju', '0007_success'),
        ('modir', '0003_adminpayment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adapt2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modir.Admin')),
                ('madadju', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='madadju.Madadju')),
            ],
        ),
    ]
