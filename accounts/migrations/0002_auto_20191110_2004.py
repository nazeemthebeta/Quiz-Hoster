# Generated by Django 2.2.6 on 2019-11-10 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='staff_name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]