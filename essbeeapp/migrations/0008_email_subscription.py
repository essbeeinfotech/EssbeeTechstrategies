# Generated by Django 4.0 on 2021-12-30 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('essbeeapp', '0007_clients'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email_subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]