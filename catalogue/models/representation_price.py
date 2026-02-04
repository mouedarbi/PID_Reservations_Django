from django.db import models
from .representation import Representation
from .price import Price

class RepresentationPrice(models.Model):
    representation = models.ForeignKey(Representation, on_delete=models.CASCADE, related_name='representation_prices')
    price = models.ForeignKey(Price, on_delete=models.CASCADE, related_name='representation_prices')

    class Meta:
        db_table = "representation_price"
        unique_together = ('representation', 'price')

    def __str__(self):
        return f"{self.representation} - {self.price}"
