# Generated by Django 3.0.9 on 2020-09-13 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcore', '0016_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extract', models.CharField(max_length=300)),
                ('code', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('draft', models.BooleanField(default=True)),
                ('visible', models.BooleanField(default=True)),
                ('article_file', models.FileField(blank=True, null=True, upload_to='blog_article')),
                ('author', models.ManyToManyField(to='lcore.Author')),
                ('tags', models.ManyToManyField(blank=True, to='lcore.Tag')),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
    ]
