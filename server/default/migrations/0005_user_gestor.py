# Generated by Django 5.1.1 on 2024-10-07 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0004_rename_taget_appstool_target'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gestor',
            field=models.BooleanField(default=False),
        ),
    ]