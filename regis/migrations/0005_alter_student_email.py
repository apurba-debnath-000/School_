# Generated by Django 4.1.7 on 2023-02-20 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regis', '0004_alter_student_std_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
