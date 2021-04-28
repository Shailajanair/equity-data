from rest_framework import serializers

from historicdata.models import HistoricData


class HistoricDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = HistoricData
        fields = '__all__'
