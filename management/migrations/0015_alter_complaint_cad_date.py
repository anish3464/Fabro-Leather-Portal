# Generated by Django 5.2 on 2025-06-24 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0014_alter_complaint_cad_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='cad_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
