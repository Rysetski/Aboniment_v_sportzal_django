from django.db import models


class Discount(models.Model):
    """Модель скидки"""
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    discount_percentage = models.FloatField()
    valid_from = models.DateField()
    valid_until = models.DateField()

    def __str__(self):
        return self.code
