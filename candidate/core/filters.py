import django_filters
from .models import *

class CareerFilter(django_filters.FilterSet):
    field = django_filters.CharFilter(field_name='cv__career__field', lookup_expr='icontains')
    experience_in_years = django_filters.NumberFilter(field_name='cv__career__experience_in_years', lookup_expr='gte')

    class Meta:
        model = Career
        fields = ['field', 'experience_in_years']