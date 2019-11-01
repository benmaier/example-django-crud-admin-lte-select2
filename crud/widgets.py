from django_select2.forms import ModelSelect2MultipleWidget, ModelSelect2Widget

# ==================== Helper Classes ===================


class SingleSelectWidget(ModelSelect2Widget):
    def filter_queryset(self, request, term, queryset, **dependent_fields):
        qs = super().filter_queryset(request, term, queryset, **dependent_fields)
        if self.ordering: 
            return qs.order_by(*self.ordering)
        return qs

class MultipleSelectWidget(ModelSelect2MultipleWidget):
    def filter_queryset(self, request, term, queryset, **dependent_fields):
        qs = super().filter_queryset(request, term, queryset, **dependent_fields)
        if self.ordering: 
            return qs.order_by(*self.ordering)
        return qs

# =============== SELECT WIDGETS FOR SPECIFIC TASKS ============

class SingleGeonameSelectWidget(SingleSelectWidget):
    search_fields = ['name__icontains']
    ordering = ['-population']

class MultipleGeonameSelectWidget(MultipleSelectWidget):
    search_fields = ['name__icontains']
    ordering = ['-population']
