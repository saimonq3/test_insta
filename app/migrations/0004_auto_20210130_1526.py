# Generated by Django 3.1.5 on 2021-01-30 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210130_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(max_length=15, unique=True, verbose_name='Название'),
        ),
    ]
