from dataclasses import fields
from rest_framework import serializers
from Dvisual_app.models import dvisual_report,d_link

class Dvisual_Report_Serializer(serializers.ModelSerializer):

    class Meta:
        model= dvisual_report
        fields = '__all__'


class D_link_Serializer(serializers.ModelSerializer):
    class Meta:
        model= d_link
        fields = '__all__'


