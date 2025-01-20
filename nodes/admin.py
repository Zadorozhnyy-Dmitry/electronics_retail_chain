from django.contrib import admin

from nodes.models import ElectronicsRetailNode

from django.urls import reverse
from django.utils.html import format_html


@admin.action(description="Очистить задолженности перед поставщиком")
def make_debt_null(modeladmin, request, queryset):
    """Очистка задолженностей перед поставщиком у выбранных объектов"""
    queryset.update(debt=None)


@admin.register(ElectronicsRetailNode)
class ElectronicsRetailNodeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "node_level",
        "node_type",
        "name",
        "city",
        # 'supplier',
        "supplier_link",
        "debt",
    )

    list_filter = ("city",)

    actions = [make_debt_null]

    def supplier_link(self, obj: ElectronicsRetailNode):
        """Отображение поставщика как ссылка"""
        if obj.supplier:
            pk = obj.supplier.id
            link = (
                f"http://127.0.0.1:8000/admin/nodes/electronicsretailnode/{pk}/change/"
            )
            return format_html('<a href="{}">{}</a>', link, obj.supplier)
        else:
            return "----"

    supplier_link.allow_tags = True
