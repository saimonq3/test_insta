# Generated by Django 3.1.5 on 2021-02-02 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210202_1323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='file',
            new_name='foto',
        ),
        migrations.AddField(
            model_name='photo',
            name='foto_resize',
            field=models.ImageField(default=None, upload_to='media/resize', verbose_name='Фотография 150'),
        ),
    ]