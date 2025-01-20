from rest_framework.serializers import ModelSerializer, SerializerMethodField

from nodes.models import ElectronicsRetailNode
from products.models import Product


class ElectronicsRetailNodeSerializer(ModelSerializer):
    """Сериализатор для узла сети"""

    class Meta:
        model = ElectronicsRetailNode
        fields = "__all__"


class ElectronicsRetailNodeCreateSerializer(ModelSerializer):
    """Сериализатор для создания узла сети"""

    class Meta:
        model = ElectronicsRetailNode
        fields = [
            "name",
            "email",
            "country",
            "city",
            "street",
            "home_number",
            "debt",
            "node_type",
            "supplier",
            "products",
        ]
