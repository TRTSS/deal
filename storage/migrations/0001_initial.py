# Generated by Django 5.0.2 on 2024-02-27 13:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0003_productphoto_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='StorageUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('XS', 'Xs'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'Xl'), ('XXL', 'Xxl')], max_length=3)),
                ('amount', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='core.product')),
            ],
        ),
    ]
