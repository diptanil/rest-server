# Generated by Django 5.0.2 on 2024-02-26 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garden', '0006_plant_remove_data_uuid_data_endpoint_data_plant'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
    ]
