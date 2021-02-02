from django_filters import FilterSet, BooleanFilter


class PhotoFilter(FilterSet):
    top_ten = BooleanFilter(method='filter_top_ten')

    def filter_top_ten(self, queryset, name, value):
        return queryset.order_by('views')[:10]