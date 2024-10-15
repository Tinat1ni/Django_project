from django.db import models


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    objects = None
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    categories = models.ManyToManyField(Category, related_name='products')

    def __str__(self):
        return self.name




