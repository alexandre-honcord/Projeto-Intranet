# Generated by Django 5.1.1 on 2024-10-07 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0006_alter_user_idtasy_alter_user_foto_alter_user_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='gestor',
        ),
    ]