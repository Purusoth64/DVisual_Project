# Generated by Django 4.2.4 on 2023-08-23 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dvisual_app', '0007_alter_dvisual_report_api_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dvisual_report_api',
            name='link',
            field=models.CharField(null=True),
        ),
    ]