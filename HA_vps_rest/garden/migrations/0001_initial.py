# Generated by Django 5.0.2 on 2024-02-26 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EndPoints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(unique=True)),
                ('name', models.CharField(max_length=140)),
                ('description', models.TextField()),
            ],
        ),
    ]
