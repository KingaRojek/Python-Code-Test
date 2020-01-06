from django_filters import FilterSet, OrderingFilter

from .models import Listing


class ListingFilter(FilterSet):
    ordering = OrderingFilter(fields=(('price', 'price'), ('created_at', 'created_at')))

    class Meta:
        model = Listing
        fields = ['ship_type__starship_class']
