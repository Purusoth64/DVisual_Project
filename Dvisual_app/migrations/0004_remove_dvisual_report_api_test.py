# Generated by Django 4.2.4 on 2023-08-21 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dvisual_app', '0003_dvisual_report_api_dvisual_config_detail_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dvisual_report_api',
            name='test',
        ),
    ]
