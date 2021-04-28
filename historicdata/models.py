from django.db import models


class HistoricData(models.Model):
    scrip_code = models.CharField(max_length=120)
    symbol = models.CharField(max_length=120)
    open_price = models.FloatField(default=0)
    high_price = models.FloatField(default=0)
    low_price = models.FloatField(default=0)
    close_price = models.FloatField(default=0)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.symbol + " : " + str(self.close_price)

    class Meta:
        db_table = 'historic_data'
