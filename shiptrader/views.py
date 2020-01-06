from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView

from .filters import ListingFilter
from .models import Listing, Starship
from .serializers import ListingSerializer, StarshipSerializer


class ListingAPIView:
    serializer_class = ListingSerializer
    queryset = Listing.objects


class ListingCreateListAPIView(ListingAPIView, CreateAPIView, ListAPIView):
    filterset_class = ListingFilter


class ListingUpdateAPIView(ListingAPIView, UpdateAPIView):
    http_method_names = ['patch']


class StarshipListAPIView(ListAPIView):
    serializer_class = StarshipSerializer
    queryset = Starship.objects
