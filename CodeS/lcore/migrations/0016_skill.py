# Generated by Django 3.0.9 on 2020-08-18 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcore', '0015_feature'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=50, unique=True)),
                ('descrip', models.CharField(blank=True, max_length=200, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['skill'],
            },
        ),
    ]
