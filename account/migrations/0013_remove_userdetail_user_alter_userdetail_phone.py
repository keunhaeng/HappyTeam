# Generated by Django 4.2.4 on 2023-08-04 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_alter_userdetail_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetail',
            name='user',
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
