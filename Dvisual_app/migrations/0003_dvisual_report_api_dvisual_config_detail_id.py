# Generated by Django 4.2.4 on 2023-08-21 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dvisual_app', '0002_remove_dvisual_report_api_dvisual_config_detail_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dvisual_report_api',
            name='dvisual_config_detail_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='dvisual', to='Dvisual_app.dvisual_config_detail'),
            preserve_default=False,
        ),
    ]
