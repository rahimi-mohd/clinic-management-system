# Generated by Django 5.1.1 on 2024-10-02 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='category',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='dosage_form',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='indication',
            field=models.CharField(max_length=50),
        ),
    ]