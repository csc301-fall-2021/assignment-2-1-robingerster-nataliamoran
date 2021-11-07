from .models import *
from rest_framework import serializers


class CovidMonitorDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CovidMonitorDate
        fields = ['id', 'title', 'date', 'country', 'province_state', "combined_key", "internal_combined_key",
                  'number', 'created_at', 'updated_at']

