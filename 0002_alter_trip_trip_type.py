# Generated by Django 4.2.20 on 2025-03-25 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_view', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='trip_type',
            field=models.CharField(choices=[('AD', 'Adventure'), ('BE', 'Beach'), ('CU', 'Cultural'), ('CR', 'Cruise'), ('EC', 'Eco'), ('FD', 'Food & Drink'), ('HI', 'Hiking'), ('SA', 'Safari'), ('SI', 'Sightseeing'), ('WE', 'Wellness')], max_length=2),
        ),
    ]
