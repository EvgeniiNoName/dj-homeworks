from rest_framework.viewsets import ModelViewSet

from measurements.models import Project, Measurement
from measurements.serializers import ProjectSerializer, MeasurementSerializer


class ProjectViewSet(ModelViewSet):
    """ViewSet для проекта."""
    projects = Project.objects.all()
    serializer_class = ProjectSerializer



class MeasurementViewSet(ModelViewSet):
    """ViewSet для измерения."""
    measurements = Measurement.objects.all()
    serializer_class = MeasurementSerializer

