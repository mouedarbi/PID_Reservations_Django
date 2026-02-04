from django.db import models
from .representation import Representation
from .reservation import Reservation
from .price import Price

class RepresentationReservation(models.Model):
    representation = models.ForeignKey(Representation, on_delete=models.CASCADE, related_name='representation_reservations')
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name='representation_reservations')
    price = models.ForeignKey(Price, on_delete=models.CASCADE, related_name='representation_reservations')
    quantity = models.PositiveSmallIntegerField()

    class Meta:
        db_table = "representation_reservation"
        constraints = [models.CheckConstraint(check=models.Q(quantity__gt=0), name="quantity_must_be_positive")]

    def __str__(self):
        return f"Reservation {self.reservation.id} - {self.representation.show.title} ({self.quantity})"
