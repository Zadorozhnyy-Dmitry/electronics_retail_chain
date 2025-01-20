from rest_framework.routers import SimpleRouter
from nodes.views import ElectronicsRetailNodeViewSet

from nodes.apps import NodesConfig

app_name = NodesConfig.name

router = SimpleRouter()
router.register("", ElectronicsRetailNodeViewSet)

urlpatterns = []
urlpatterns += router.urls
