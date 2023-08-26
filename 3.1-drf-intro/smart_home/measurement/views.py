from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView, ListAPIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer


# получение датчиков, создание датчика
class SensorCreate(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# обновление датчика
class SensorUpdate(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    #
    #
    # def get(self, request, *args, **kwargs):
    #     print(Sensor.objects.filter(id=15))
    #     # # print(Sensor.objects.filter(id=15))
    #     # # print(self.request.user)
    #     return self.retrieve(request, *args, **kwargs)

# добавление измерения
class MeasurementAdded(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
