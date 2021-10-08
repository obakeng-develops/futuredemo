# Generated by Django 3.2.8 on 2021-10-08 08:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requests',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_client', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='requests',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_manager', to=settings.AUTH_USER_MODEL),
        ),
    ]
