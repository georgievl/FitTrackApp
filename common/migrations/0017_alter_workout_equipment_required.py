# Generated by Django 5.2.4 on 2025-07-24 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0016_workout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='equipment_required',
            field=models.CharField(max_length=100),
        ),
    ]
