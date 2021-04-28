from django.contrib import admin
from historicdata.models import HistoricData


@admin.register(HistoricData)
class BookAdmin(admin.ModelAdmin):
    pass
