# Generated by Django 2.2.21 on 2021-06-15 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saloni',
            name='Descrizione',
            field=models.CharField(max_length=60),
        ),
    ]
