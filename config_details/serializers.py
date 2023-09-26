from dataclasses import fields
from rest_framework import serializers
from Dvisual_app.models import dvisual_config_detail

class Dvisual_Config_Details_Serializer(serializers.ModelSerializer):

    class Meta:
        model= dvisual_config_detail
        fields = '__all__'

