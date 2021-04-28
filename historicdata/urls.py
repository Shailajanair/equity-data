from django.urls import path, include
from rest_framework import routers

from historicdata import views

router = routers.DefaultRouter()
router.register('custom_user', views.HistoricDataStocksViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
