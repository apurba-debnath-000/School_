# Generated by Django 4.1.7 on 2023-02-20 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_id', models.CharField(default='no id given', max_length=20)),
                ('name', models.CharField(default='No name', max_length=50)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]
