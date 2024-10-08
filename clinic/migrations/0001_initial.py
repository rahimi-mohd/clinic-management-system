# Generated by Django 5.1.1 on 2024-10-02 07:21

import datetime
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.IntegerField(choices=[(1, 'Analgesic'), (2, 'Antibiotic'), (3, 'Antidepressant'), (4, 'Antidiabetic'), (5, 'Antifungal'), (6, 'Antipyretic'), (7, 'Antiseptic'), (8, 'Antiviral')], default=1)),
                ('dosage_form', models.IntegerField(choices=[(1, 'Capsule'), (2, 'Cream'), (3, 'Drops'), (4, 'Inhaler'), (5, 'Injection'), (6, 'Ointment'), (7, 'Syrup'), (8, 'Tablet')], default=1)),
                ('indication', models.IntegerField(choices=[(1, 'Depression'), (2, 'Diabetes'), (3, 'Fever'), (4, 'Fungus'), (5, 'Infection'), (6, 'Pain'), (7, 'Virus'), (8, 'Wound')], default=1)),
                ('strength', models.IntegerField(default=1)),
                ('quantity_in_stock', models.IntegerField(default=0)),
            ],
        ),
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
                ('medical_leave', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
                ('medicine', models.ManyToManyField(to='clinic.medicine')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Checkin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'waiting'), (2, 'done')], default=1)),
                ('date', models.DateField(auto_now_add=True)),
                ('medical_record', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='clinic.medicalrecord')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.IntegerField(choices=[(1, 'unpaid'), (2, 'paid')], default=1)),
                ('payment_type', models.IntegerField(choices=[(1, 'cash'), (2, 'card')], default=1)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('medical_record', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='clinic.medicalrecord')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('time_slot', models.IntegerField(choices=[(0, '9:00 - 10:00'), (1, '10:00 - 11:00'), (2, '11:00 - 12:00'), (3, '12:00 - 01:00'), (4, '03:00 - 04:00'), (5, '04:00 - 05:00'), (6, '05:00 - 06:00')])),
                ('status', models.IntegerField(choices=[(1, 'Scheduled'), (2, 'Completed'), (3, 'No Show')], default=1)),
                ('date', models.DateField(default=datetime.date.today)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.patient')),
            ],
            options={
                'unique_together': {('time_slot', 'date')},
            },
        ),
    ]
