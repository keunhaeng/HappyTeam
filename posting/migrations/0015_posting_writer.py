# Generated by Django 4.2.3 on 2023-08-01 00:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posting', '0014_alter_image_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='posting',
            name='writer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='postings', to=settings.AUTH_USER_MODEL),
        ),
    ]
