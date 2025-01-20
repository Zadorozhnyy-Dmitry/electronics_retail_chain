from rest_framework.serializers import ModelSerializer

from nodes.models import ElectronicsRetailNode


class ElectronicsRetailNodeSerializer(ModelSerializer):
    """Сериализатор для узла сети"""

    class Meta:
        model = ElectronicsRetailNode
        fields = '__all__'
