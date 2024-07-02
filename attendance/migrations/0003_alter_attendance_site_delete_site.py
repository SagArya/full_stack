# Generated by Django 5.0.6 on 2024-07-02 14:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_salary_paid'),
        ('my_sites', '0003_rename_image_materialreport_material_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_sites.site'),
        ),
        migrations.DeleteModel(
            name='Site',
        ),
    ]
