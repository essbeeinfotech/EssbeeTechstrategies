# Generated by Django 4.0 on 2021-12-29 09:54

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('desc', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('more_desc', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('img', models.ImageField(upload_to='blog/')),
                ('author', models.CharField(default=None, max_length=100)),
                ('date', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Blogs',
                'ordering': ('-date',),
            },
        ),
    ]
