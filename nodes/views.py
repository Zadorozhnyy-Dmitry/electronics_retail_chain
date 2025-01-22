from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from nodes.models import ElectronicsRetailNode
from nodes.serializers import (
    ElectronicsRetailNodeSerializer,
    ElectronicsRetailNodeCreateSerializer,
    ElectronicsRetailNodeUpdateSerializer,
)
from rest_framework.generics import ListAPIView


class ElectronicsRetailSuppliersViewSet(ListAPIView):
    """Контроллер только для поставщиков"""

    queryset = ElectronicsRetailNode.objects.exclude(node_level=2)
    serializer_class = ElectronicsRetailNodeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "country",
    ]


class ElectronicsRetailNodeViewSet(ModelViewSet):
    """Контроллер для узла сети"""

    queryset = ElectronicsRetailNode.objects.all()

    # Выбор сериализатора
    def get_serializer_class(self):
        if self.action == "create":
            return ElectronicsRetailNodeCreateSerializer
        elif self.action == "partial_update" or self.action == "update":
            return ElectronicsRetailNodeUpdateSerializer
        return ElectronicsRetailNodeSerializer

    # Фильтрация
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "country",
    ]

    def perform_create(self, serializer):
        """Автоматическая запись пользователя в атрибут owner при создании объекта товара"""
        """Автоматическая запись уровня иерархии"""
        node = serializer.save()
        node.owner = self.request.user
        if node.supplier:
            node.node_level = node.supplier.node_level + 1
        else:
            node.node_level = 0
            node.node_type = 'f'
        node.save()
