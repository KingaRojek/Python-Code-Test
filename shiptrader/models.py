from django.db import models


class Starship(models.Model):
    name = models.CharField(max_length=255, unique=True)
    starship_class = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)

    length = models.FloatField(null=True)
    hyperdrive_rating = models.FloatField(null=True)
    cargo_capacity = models.BigIntegerField(null=True)

    crew = models.IntegerField(null=True)
    passengers = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Listing(models.Model):
    name = models.CharField(max_length=255)
    ship_type = models.ForeignKey(Starship, related_name='listings')
    price = models.IntegerField()
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
