from django.urls import reverse
from model_mommy import mommy
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Listing, Starship


class ListingCreateListAPIViewAPITestCase(APITestCase):
    def test_create(self):
        starship = mommy.make(Starship)
        data = {'name': 'test', 'price': 0, 'ship_type': starship.name}
        url = reverse('listing-create-list')
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Listing.objects.count(), 1)
        obj = Listing.objects.get()
        self.assertEqual(obj.name, data['name'])
        self.assertEqual(obj.price, data['price'])
        self.assertEqual(obj.ship_type, starship)

    def test_list(self):
        quantity = 3
        mommy.make(Listing, _quantity=quantity)
        url = reverse('listing-create-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), quantity)


class ListingUpdateAPIViewTestCase(APITestCase):
    def test_update(self):
        listing = mommy.make(Listing, price=0)
        data = {'price': 1}
        url = reverse('listing-update', args=[listing.pk])
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Listing.objects.get().price, data['price'])


class StarshipListAPIViewAPITestCase(APITestCase):
    def test_list(self):
        quantity = 3
        mommy.make(Starship, _quantity=quantity)
        response = self.client.get(reverse('starship-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), quantity)
