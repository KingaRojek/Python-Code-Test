from django.conf.urls import url

from .views import ListingCreateListAPIView, ListingUpdateAPIView, StarshipListAPIView

urlpatterns = [
    url('^listing/$', ListingCreateListAPIView.as_view(), name='listing-create-list'),
    url(
        '^listing/(?P<pk>\d+)/$', ListingUpdateAPIView.as_view(), name='listing-update'
    ),
    url('^starship/$', StarshipListAPIView.as_view(), name='starship-list'),
]
