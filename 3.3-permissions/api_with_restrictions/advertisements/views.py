from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsCreatorOrReadOnly
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsCreatorOrReadOnly]
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsCreatorOrReadOnly()]
        return []
