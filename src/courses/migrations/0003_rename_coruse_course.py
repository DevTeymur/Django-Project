# Generated by Django 3.2.5 on 2021-07-15 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_coruse_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Coruse',
            new_name='Course',
        ),
    ]