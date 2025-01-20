from rest_framework.routers import SimpleRouter

from products.views import ProductViewSet
from products.apps import ProductsConfig

app_name = ProductsConfig.name

router = SimpleRouter()
router.register('', ProductViewSet)

urlpatterns = []
urlpatterns += router.urls
