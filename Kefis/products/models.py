from django.db import models

# Create your models here.

class Product(models.Model):
	name = models.CharField(max_length = 70)
	units_of_measure = models.CharField(max_length = 50)
	price = models.IntegerField()
	quantity = models.IntegerField()
	default_quantity = models.IntegerField()
	reorder_level = models.IntegerField()


class Sales(models.Model):
	quantity_sold = models.IntegerField()





def __str__(self):
	return self.name	