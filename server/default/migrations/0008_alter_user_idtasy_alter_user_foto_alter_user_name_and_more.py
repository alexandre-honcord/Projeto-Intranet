# Generated by Django 5.1.1 on 2024-10-08 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0007_remove_user_gestor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='IDtasy',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='foto',
            field=models.ImageField(default=1, upload_to='default/users/photos/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='senha',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]