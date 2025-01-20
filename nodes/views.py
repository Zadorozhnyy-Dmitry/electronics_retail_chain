from rest_framework.viewsets import ModelViewSet
from nodes.models import ElectronicsRetailNode
from nodes.serializers import ElectronicsRetailNodeSerializer


class ElectronicsRetailNodeViewSet(ModelViewSet):
    """Контроллер для узла сети"""
    queryset = ElectronicsRetailNode.objects.all()
    serializer_class = ElectronicsRetailNodeSerializer

    def perform_create(self, serializer):
        """Автоматическая запись пользователя в атрибут owner при создании объекта товара"""
        """Автоматическая запись уровня иерархии"""
        node = serializer.save()
        # node.owner = self.request.user
        if node.supplier:
            node.node_level = node.supplier.node_level + 1
        node.save()
