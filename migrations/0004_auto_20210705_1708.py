# Generated by Django 2.2.21 on 2021-07-05 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210615_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuntamenti',
            name='Data',
            field=models.DateTimeField(blank=True),
        ),
    ]