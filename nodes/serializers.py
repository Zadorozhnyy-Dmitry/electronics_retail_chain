from rest_framework import serializers

from nodes.models import ElectronicsRetailNode


class ElectronicsRetailNodeSerializer(serializers.ModelSerializer):
    """Сериализатор для узла сети"""

    class Meta:
        model = ElectronicsRetailNode
        fields = "__all__"


class ElectronicsRetailNodeUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор для узла сети - запрет на редактирование поля задолженности"""

    debt = serializers.DecimalField(max_digits=15, decimal_places=2, read_only=True)

    class Meta:
        model = ElectronicsRetailNode
        fields = "__all__"


class ElectronicsRetailNodeCreateSerializer(serializers.ModelSerializer):
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
