import logging
from typing import Any, Dict

import swapi
from django.core.management.base import BaseCommand
from django.db import models

from shiptrader.models import Starship

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Import starships from swapi'

    # concrete_fields is an internal django api and may change in future
    model_fields = Starship._meta.concrete_fields

    def normalize_api_starship(self, starship: swapi.models.Starship) -> Dict[str, Any]:
        """
        Make dict that can be used to create a Starship model instance. 
        """
        normalized = {}
        for field in self.model_fields:
            api_value = getattr(starship, field.name, None)

            # normalize data
            if api_value == 'unknown':
                api_value = None
            elif isinstance(field, models.FloatField) and isinstance(api_value, str):
                api_value = api_value.replace(',', '')
            normalized[field.name] = api_value

            logger.debug(f'Normalized starship data: {normalized}')

        return normalized

    def handle(self, *args, **options):
        # get data from api
        api_starships = swapi.get_all('starships').items

        objs = Starship.objects.bulk_create(
            (
                Starship(**self.normalize_api_starship(starship))
                for starship in api_starships
            )
        )

        self.stdout.write(self.style.SUCCESS(f'Created {objs}'))
