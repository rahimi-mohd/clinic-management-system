# Generated by Django 5.1.1 on 2024-10-02 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0002_alter_medicine_category_alter_medicine_dosage_form_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalrecord',
            name='medicine',
            field=models.ManyToManyField(blank=True, null=True, to='clinic.medicine'),
        ),
    ]
