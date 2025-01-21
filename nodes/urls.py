from django.urls import path
from rest_framework.routers import SimpleRouter
from nodes.views import ElectronicsRetailNodeViewSet, ElectronicsRetailSuppliersViewSet

from nodes.apps import NodesConfig

app_name = NodesConfig.name

router = SimpleRouter()
router.register("", ElectronicsRetailNodeViewSet)

urlpatterns = [
    # маршрутизатор списка только поставщиков
    path("suppliers/", ElectronicsRetailSuppliersViewSet.as_view(), name="suppliers-list"),
]
urlpatterns += router.urls
