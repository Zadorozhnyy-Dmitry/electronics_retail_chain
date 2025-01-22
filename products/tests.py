from rest_framework.test import APITestCase

from products.models import Product
from users.models import User


class ProductModelTestCase(APITestCase):
    """Тест модели товара"""

    def setUp(self):
        """Фикстуры"""
        self.user = User.objects.create(username='test', password='test')
        self.client.force_authenticate(user=self.user)

    def test_model(self):
        """Тест создания товара"""
        product = Product.objects.create(
            name='name',
            model='model',
            release_data='2025-01-20',
            price=100.00,
            owner=self.user,
        )
        self.assertEqual(product.name, 'name')
        self.assertEqual(product.model, 'model')
        self.assertEqual(product.release_data, '2025-01-20')
        self.assertEqual(product.price, 100.00)
        self.assertEqual(product.owner, self.user)

