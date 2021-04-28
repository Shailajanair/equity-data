from rest_framework import viewsets

from historicdata.models import HistoricData
from historicdata.serializer import HistoricDataSerializer
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


class HistoricDataStocksViewSet(viewsets.ModelViewSet):
    serializer_class = HistoricDataSerializer
    queryset = HistoricData.objects.all()

    def get_queryset(self):
        query_set = self.queryset
        symbol = self.request.GET.get('symbol')
        if cache.get(symbol):
            serialized_data = cache.get(symbol)
        else:
            query_set = query_set.filter(symbol=symbol).first()
            serialized_data = HistoricDataSerializer(query_set, many=True).data
            cache.set(symbol, serialized_data)

        return serialized_data
