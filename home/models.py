from django.db import models

# Create your models here.
PRODUCT_TYPE = [
    ('Beauty', 'Beauty'),
    ('Electronic', 'Electronic'),
    ('CLothing', 'Clothing'),
    ('Shoes', 'Shoes'),
    ('Cars', 'Cars'),
]


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.FloatField()
    image = models.ImageField(upload_to='images/')
    stock = models.IntegerField()
    type = models.CharField(max_length=100, choices=PRODUCT_TYPE)

    def __str__(self):
        return self.name
