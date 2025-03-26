# Generated by Django 5.0.6 on 2024-06-07 02:32

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dasboart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='jenis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=8)),
            ],
        ),
        migrations.AddField(
            model_name='barang',
            name='waktu_posting',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='barang',
            name='jenis_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dasboart.jenis'),
        ),
    ]
