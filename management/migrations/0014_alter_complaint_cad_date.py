# Generated by Django 5.2 on 2025-06-24 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0013_complaint_cad_date_complaint_updated_order_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='cad_date',
            field=models.DateField(null=True),
        ),
    ]
