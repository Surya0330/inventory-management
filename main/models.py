from django.db import models

# Create your models here.



class Brands(models.Model):
    brand = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.brand} {self.model}"