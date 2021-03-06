# Generated by Django 4.0 on 2021-12-29 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('essbeeapp', '0002_blog_sub_head'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('from_email', models.EmailField(max_length=254)),
                ('mobile_num', models.CharField(max_length=15, null=True)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Contacts',
            },
        ),
    ]
