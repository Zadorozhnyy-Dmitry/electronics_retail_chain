from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    """Сериализатор для пользователя"""

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "is_active",
            "is_superuser",
            "last_login",
        )


class UserCreateSerializer(ModelSerializer):
    """Сериализатор для регистрации пользователя"""

    class Meta:
        model = User
        fields = (
            "username",
            "password",
        )
