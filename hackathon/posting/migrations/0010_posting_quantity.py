# Generated by Django 4.2.3 on 2023-07-30 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0009_remove_image_data_remove_image_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='posting',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]