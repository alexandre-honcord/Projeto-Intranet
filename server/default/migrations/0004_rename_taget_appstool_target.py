# Generated by Django 5.1.1 on 2024-10-01 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0003_appstool_taget'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appstool',
            old_name='taget',
            new_name='target',
        ),
    ]