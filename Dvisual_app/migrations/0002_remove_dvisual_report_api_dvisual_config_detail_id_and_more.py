# Generated by Django 4.2.4 on 2023-08-21 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dvisual_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dvisual_report_api',
            name='dvisual_config_detail_id',
        ),
        migrations.AddField(
            model_name='dvisual_report_api',
            name='test',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='dvisual_config', to='Dvisual_app.dvisual_config'),
            preserve_default=False,
        ),
    ]
