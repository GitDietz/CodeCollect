# Generated by Django 3.0.9 on 2020-09-20 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcore', '0019_auto_20200920_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='description',
            field=models.CharField(default='something', max_length=300),
            preserve_default=False,
        ),
    ]
