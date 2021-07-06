# Generated by Django 2.2.21 on 2021-07-05 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210705_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saloni',
            name='OrarioAperturaMattino',
            field=models.CharField(choices=[('07:00:00 AM', '07:00:00 AM'), ('07:30:00 AM', '07:30:00 AM'), ('08:00:00 AM', '08:00:00 AM'), ('08:30:00 AM', '08:30:00 AM'), ('09:00:00 AM', '09:00:00 AM'), ('09:30:00 AM', '09:30:00 AM'), ('10:00:00 AM', '10:00:00 AM'), ('10:30:00 AM', '10:30:00 AM'), ('11:00:00 AM', '11:00:00 AM'), ('11:30:00 AM', '11:30:00 AM'), ('12:00:00 AM', '12:00:00 AM'), ('12:30:00 AM', '12:30:00 AM'), ('01:00:00 PM', '01:00:00 PM'), ('01:30:00 PM', '01:30:00 PM'), ('03:00:00 PM', '03:00:00 PM'), ('03:30:00 PM', '03:30:00 PM'), ('04:00:00 PM', '04:00:00 PM'), ('04:30:00 PM', '04:30:00 PM'), ('05:00:00 PM', '05:00:00 PM'), ('05:30:00 PM', '05:30:00 PM'), ('06:00:00 PM', '06:00:00 PM'), ('06:30:00 PM', '06:30:00 PM'), ('07:00:00 PM', '07:00:00 PM'), ('07:30:00 PM', '07:30:00 PM'), ('08:00:00 PM', '08:00:00 PM'), ('08:30:00 PM', '08:30:00 PM')], max_length=11),
        ),
        migrations.AlterField(
            model_name='saloni',
            name='OrarioAperturaPomeriggio',
            field=models.CharField(choices=[('07:00:00 AM', '07:00:00 AM'), ('07:30:00 AM', '07:30:00 AM'), ('08:00:00 AM', '08:00:00 AM'), ('08:30:00 AM', '08:30:00 AM'), ('09:00:00 AM', '09:00:00 AM'), ('09:30:00 AM', '09:30:00 AM'), ('10:00:00 AM', '10:00:00 AM'), ('10:30:00 AM', '10:30:00 AM'), ('11:00:00 AM', '11:00:00 AM'), ('11:30:00 AM', '11:30:00 AM'), ('12:00:00 AM', '12:00:00 AM'), ('12:30:00 AM', '12:30:00 AM'), ('01:00:00 PM', '01:00:00 PM'), ('01:30:00 PM', '01:30:00 PM'), ('03:00:00 PM', '03:00:00 PM'), ('03:30:00 PM', '03:30:00 PM'), ('04:00:00 PM', '04:00:00 PM'), ('04:30:00 PM', '04:30:00 PM'), ('05:00:00 PM', '05:00:00 PM'), ('05:30:00 PM', '05:30:00 PM'), ('06:00:00 PM', '06:00:00 PM'), ('06:30:00 PM', '06:30:00 PM'), ('07:00:00 PM', '07:00:00 PM'), ('07:30:00 PM', '07:30:00 PM'), ('08:00:00 PM', '08:00:00 PM'), ('08:30:00 PM', '08:30:00 PM')], max_length=11),
        ),
        migrations.AlterField(
            model_name='saloni',
            name='OrarioChiusurMattino',
            field=models.CharField(choices=[('07:00:00 AM', '07:00:00 AM'), ('07:30:00 AM', '07:30:00 AM'), ('08:00:00 AM', '08:00:00 AM'), ('08:30:00 AM', '08:30:00 AM'), ('09:00:00 AM', '09:00:00 AM'), ('09:30:00 AM', '09:30:00 AM'), ('10:00:00 AM', '10:00:00 AM'), ('10:30:00 AM', '10:30:00 AM'), ('11:00:00 AM', '11:00:00 AM'), ('11:30:00 AM', '11:30:00 AM'), ('12:00:00 AM', '12:00:00 AM'), ('12:30:00 AM', '12:30:00 AM'), ('01:00:00 PM', '01:00:00 PM'), ('01:30:00 PM', '01:30:00 PM'), ('03:00:00 PM', '03:00:00 PM'), ('03:30:00 PM', '03:30:00 PM'), ('04:00:00 PM', '04:00:00 PM'), ('04:30:00 PM', '04:30:00 PM'), ('05:00:00 PM', '05:00:00 PM'), ('05:30:00 PM', '05:30:00 PM'), ('06:00:00 PM', '06:00:00 PM'), ('06:30:00 PM', '06:30:00 PM'), ('07:00:00 PM', '07:00:00 PM'), ('07:30:00 PM', '07:30:00 PM'), ('08:00:00 PM', '08:00:00 PM'), ('08:30:00 PM', '08:30:00 PM')], max_length=11),
        ),
        migrations.AlterField(
            model_name='saloni',
            name='OrarioChiusuraPomeriggio',
            field=models.CharField(choices=[('07:00:00 AM', '07:00:00 AM'), ('07:30:00 AM', '07:30:00 AM'), ('08:00:00 AM', '08:00:00 AM'), ('08:30:00 AM', '08:30:00 AM'), ('09:00:00 AM', '09:00:00 AM'), ('09:30:00 AM', '09:30:00 AM'), ('10:00:00 AM', '10:00:00 AM'), ('10:30:00 AM', '10:30:00 AM'), ('11:00:00 AM', '11:00:00 AM'), ('11:30:00 AM', '11:30:00 AM'), ('12:00:00 AM', '12:00:00 AM'), ('12:30:00 AM', '12:30:00 AM'), ('01:00:00 PM', '01:00:00 PM'), ('01:30:00 PM', '01:30:00 PM'), ('03:00:00 PM', '03:00:00 PM'), ('03:30:00 PM', '03:30:00 PM'), ('04:00:00 PM', '04:00:00 PM'), ('04:30:00 PM', '04:30:00 PM'), ('05:00:00 PM', '05:00:00 PM'), ('05:30:00 PM', '05:30:00 PM'), ('06:00:00 PM', '06:00:00 PM'), ('06:30:00 PM', '06:30:00 PM'), ('07:00:00 PM', '07:00:00 PM'), ('07:30:00 PM', '07:30:00 PM'), ('08:00:00 PM', '08:00:00 PM'), ('08:30:00 PM', '08:30:00 PM')], max_length=11),
        ),
    ]
