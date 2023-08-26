from django.urls import path

from measurement.views import SensorCreate, SensorUpdate, MeasurementAdded

urlpatterns = [
    path('sensors/', SensorCreate.as_view()),
    path('sensors/<pk>/', SensorUpdate.as_view()),
    path('measurements/', MeasurementAdded.as_view()),
]
