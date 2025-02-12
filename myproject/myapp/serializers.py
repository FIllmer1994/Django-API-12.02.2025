from rest_framework import serializers
from .models import Forecast
class ForecastSerializer(serializers.ModelSerializer):
    values = serializers.ListField(child=serializers.FloatField())
    class Meta:
        model = Forecast
        fields = ["id", "company_id", "forecast_date", "values"]