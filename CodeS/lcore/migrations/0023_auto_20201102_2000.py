# Generated by Django 3.0.9 on 2020-11-02 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcore', '0022_auto_20201030_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appfeature',
            name='last_test',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]