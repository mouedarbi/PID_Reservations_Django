from django.db import models
from .reservation import Reservation
from .representation import Representation
from .price import Price


class RepresentationReservation(models.Model):
    """
    Table de liaison entre réservation, représentation et prix
    """
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name='representation_reservations')
    representation = models.ForeignKey(Representation, on_delete=models.CASCADE, related_name='reservation_links')
    price = models.ForeignKey(Price, on_delete=models.CASCADE, related_name='representation_reservations')
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.reservation.id} - {self.representation.id} - {self.price.type}"

    class Meta:
        db_table = "reservations_representation_reservation"
        constraints = [
            models.CheckConstraint(
                check=models.Q(quantity__gt=0),
                name="quantity_must_be_positive"
            )
        ]