# Generated by Django 3.2.8 on 2021-10-08 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_alter_requests_request_date'),
        ('client', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='request',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.requests'),
        ),
        migrations.AlterField(
            model_name='document',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
