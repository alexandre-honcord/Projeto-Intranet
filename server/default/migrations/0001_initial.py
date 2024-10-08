# Generated by Django 4.2.13 on 2024-07-04 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('links', models.TextField()),
                ('image', models.ImageField(upload_to='default/tools/images/')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IDtasy', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('senha', models.CharField(max_length=50)),
                ('foto', models.ImageField(upload_to='default/users/photos/')),
                ('last_login', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
