from django.db import models
from datetime import date
try:
    from django.db.models import JSONField
except ImportError:
    from django.contrib.postgres.fields import JSONField

class dvisual_config(models.Model):
    # connections_id=models.AutoField(auto_created=True,primary_key=True,serialize=True,verbose_name='ID')
    # connection_id = models.CharField(max_length=100)

    dvisual_config_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    logo_name = models.CharField(max_length=100)
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    key_param = JSONField()
    d_type = JSONField()

    def _str_(self):
        return self.dvisual_config_name

    def deactivate_expired_connections(self):
        now = date.today()
        if self.end_date < now:
            self.is_active = False
            self.save()

    class Meta:
        db_table = "dvisual_config"


class dvisual_config_detail(models.Model):
    dvisual_config_id = models.ForeignKey(dvisual_config, on_delete=models.CASCADE, related_name='dvisual_config_id')
    conn_str = JSONField()
    dvisual_config_detail = models.CharField(max_length=100)
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField()
    last_modified_by = models.CharField(max_length=100, null=True)
    last_modified_on = models.DateField(auto_now=True, null=True)
    created_on = models.DateField(auto_now=True, null=True)
    created_by = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)

    def _str_(self):
        return self.dvisual_config_detail

    def deactivate_expired_connections(self):
        now = date.today()
        if self.end_date < now:
            self.is_active = False
            self.save()

    class Meta:
        db_table = 'dvisual_config_detail'

class dvisual_report(models.Model):
    dvisual_config_detail_id=models.ForeignKey(dvisual_config_detail, on_delete=models.CASCADE, related_name='dvisual')
    dvisual_report_name = models.CharField(max_length=200)
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField()
    workbook_name = models.CharField(max_length=200)
    r_link=models.CharField(null=True)

    def _str_(self):
        return self.dvisual_report_name

    def deactivate_expired_connections(self):
        now = date.today()
        if self.end_date < now:
            self.is_active = False
            self.save()

    class Meta:
        db_table = 'dvisual_report'


class d_link(models.Model):
    dvisual_report_id=models.ForeignKey(dvisual_report, on_delete=models.CASCADE, related_name='link')
    link_1=models.CharField(null=True)

    def _str_(self):
        return self.link_1

    class Meta:
        db_table = 'd_link'
