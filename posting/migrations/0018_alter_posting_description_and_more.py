# Generated by Django 4.2.4 on 2023-08-16 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0017_image_saved_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='posting',
            name='example_description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
