# Generated by Django 5.0.2 on 2024-02-26 04:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garden', '0003_endpoint_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temparature', models.FloatField(default=None)),
                ('humidity', models.FloatField(default=None)),
                ('ph', models.FloatField(default=None)),
                ('moisture', models.FloatField(default=None)),
                ('uuid', models.ForeignKey(db_column='uuid', on_delete=django.db.models.deletion.CASCADE, to='garden.endpoint', to_field='uuid')),
            ],
        ),
    ]
