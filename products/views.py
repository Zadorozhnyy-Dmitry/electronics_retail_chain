from rest_framework.viewsets import ModelViewSet
from products.models import Product
from products.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    """Контроллер для товара"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        """Автоматическая запись пользователя в атрибут owner при создании объекта товара"""
        product = serializer.save()
        product.owner = self.request.user
        product.save()
