# Generated by Django 5.1.1 on 2024-09-23 11:28

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.IntegerField(blank=True, choices=[(1, 'Mr.'), (2, 'Mrs.'), (3, 'Ms.')], default=1, null=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('ic_number', models.CharField(max_length=12, unique=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('phone_number', models.CharField(max_length=20, unique=True)),
                ('register_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='register_date')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('record_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='record_date')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('time_slot', models.IntegerField(choices=[(0, '9:00 - 10:00'), (1, '10:00 - 11:00'), (2, '11:00 - 12:00'), (3, '12:00 - 01:00'), (4, '03:00 - 04:00'), (5, '04:00 - 05:00'), (6, '05:00 - 06:00')])),
                ('status', models.IntegerField(choices=[(1, 'Scheduled'), (2, 'Completed'), (3, 'No Show')], default=1)),
                ('date', models.DateField(auto_now_add=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.patient')),
            ],
            options={
                'unique_together': {('time_slot', 'date')},
            },
        ),
    ]
