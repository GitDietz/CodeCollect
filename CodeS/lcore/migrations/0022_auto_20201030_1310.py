# Generated by Django 3.0.9 on 2020-10-30 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcore', '0021_appfeature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appfeature',
            name='last_bug',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='appfeature',
            name='last_test',
            field=models.DateTimeField(blank=True),
        ),
    ]