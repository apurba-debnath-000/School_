# Generated by Django 4.1.7 on 2023-03-03 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pupils',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=80)),
                ('p_email', models.EmailField(max_length=254)),
                ('p_roll', models.IntegerField()),
                ('p_course', models.CharField(max_length=60)),
                ('p_password', models.CharField(max_length=20)),
            ],
        ),
    ]
