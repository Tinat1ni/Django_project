from django.db import models

class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=30)
    total_amount = models.FloatField()
    customer_adress = models.CharField(max_length=100)

    def __str__(self):
        return self.id, self.customer_name, self.total_amount




