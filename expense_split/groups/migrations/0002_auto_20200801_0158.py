# Generated by Django 3.0.3 on 2020-08-01 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='password',
            field=models.CharField(max_length=200),
        ),
    ]
