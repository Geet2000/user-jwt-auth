# Generated by Django 3.2.5 on 2021-09-30 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0006_customuser_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='address',
            field=models.CharField(max_length=200),
        ),
    ]
