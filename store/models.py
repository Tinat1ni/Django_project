from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    adress = models.CharField(max_length=40)

    def __str__(self):
        return self.name, self.description, self.adress


