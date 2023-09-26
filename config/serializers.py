from rest_framework import serializers
from Dvisual_app.models import dvisual_config

class dvisual_config_Serializer(serializers.ModelSerializer):
    class Meta:
        model = dvisual_config
        fields = "__all__"