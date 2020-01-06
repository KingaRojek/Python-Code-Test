from django.core.exceptions import ValidationError
from rest_framework import serializers

from .models import Listing, Starship


class ListingSerializer(serializers.ModelSerializer):
    ship_type = serializers.CharField(required=True)

    class Meta:
        model = Listing
        fields = '__all__'

    def validate_ship_type(self, data):
        obj = Starship.objects.filter(name=data).first()
        if obj is None:
            raise ValidationError(
                f'Invalid ship name "{data}" - object does not exist.'
            )
        return obj


class StarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Starship
        fields = '__all__'
